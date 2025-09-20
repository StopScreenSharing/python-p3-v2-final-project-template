from . import CURSOR, CONN

class Gardener:

    def __init__(self, name, phone, id=None):
        self.id = id
        self.name = name
        self.phone = phone

#Class methods

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS gardeners (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT
            );
        """)
        CONN.commit()
    
    @classmethod
    def create(cls, name, phone):
        CURSOR.execute("""
            INSERT INTO gardeners (name, phone)
            VALUES (?, ?);
        """, (name, phone))
        CONN.commit()
        new_id = CURSOR.lastrowid
        return cls(name, phone, id=new_id)

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM gardeners;")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], phone=row[2]) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM gardeners WHERE id=?;", (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], name=row[1], phone=row[2]) if row else None
    
    def delete(self):
        if self.id:
            from .plant import Plant
            
            for plant in self.plants:
                plant.delete()
            
            CURSOR.execute("DELETE FROM gardeners WHERE id=?;", (self.id,))
            CONN.commit()
            print(f"Gardener {self.name} and their plants deleted.")
            self.id = None
    

    # Properties

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must not be empty.")
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        if isinstance(value, str) and value.isdigit():
            self._phone = value
        else:
            raise ValueError("Phone must be a number.")
    @property
    def plants(self):
        from .plant import Plant
        return [plant for plant in Plant.get_all() if plant.gardener_id == self.id]
    
    def __repr__(self):
        return f"<Gardener {self.id}: {self.name}, {self.phone}>"