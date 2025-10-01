from models import CURSOR, CONN

class Gardener:
    def __init__(self, name, phone, id=None):
        self.id = id
        self.name = name
        self.phone = phone 

    # Properties
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "" or value.isdigit():
            raise ValueError("Please enter a name!")
        self._name = value.strip()
        
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, int):
            raise ValueError("Phone number must be an integer.")
        self._phone = value

   # Class methods 
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS gardeners (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone INTEGER
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS gardeners;"
        CURSOR.execute(sql)
        CONN.commit()

    # Others
    def save(self):
        if self.id:
            self.update()
        else:
            sql = "INSERT INTO gardeners (name, phone) VALUES (?, ?);"
            CURSOR.execute(sql, (self.name, self.phone))
            CONN.commit()
            self.id = CURSOR.lastrowid

    def update(self):
        sql = "UPDATE gardeners SET name = ?, phone = ? WHERE id = ?;"
        CURSOR.execute(sql, (self.name, self.phone, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM gardeners WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM gardeners;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls(id=row[0], name=row[1], phone=row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM gardeners WHERE id = ?;"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(id=row[0], name=row[1], phone=row[2]) if row else None