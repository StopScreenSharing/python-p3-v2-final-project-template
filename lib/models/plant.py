
from . import CURSOR, CONN

class Plant:

    def __init__(self, species, height, gardener_id, id=None):
        self.id = id
        self.species = species
        self.height = height
        self.gardener_id = gardener_id
        
    
    # Class Methods

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS plants (
                id INTEGER PRIMARY KEY,
                species TEXT,
                height INTEGER,
                gardener_id INTEGER,
                FOREIGN KEY (gardener_id) REFERENCES gardeners(id)
            );
        """)
        CONN.commit()

    @classmethod
    def create(cls, species, height, gardener_id):
        CURSOR.execute("""
            INSERT INTO plants (species, height, gardener_id)
            VALUES (?, ?, ?);
        """, (species, height, gardener_id))
        CONN.commit()
        new_id = CURSOR.lastrowid
        return cls(species, height, gardener_id, id = new_id)

    @classmethod
    def find_by_species(cls, species):
        CURSOR.execute("SELECT * FROM plants WHERE LOWER(species)=?;", (species.lower(),))
        rows = CURSOR.fetchall()
        return [cls(id=row[0], species=row[1], height=row[2], gardener_id=row[3]) for row in rows]
      
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM plants;")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], species=row[1], height=row[2], gardener_id=row[3]) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM plants WHERE id=?;", (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], species=row[1], height=row[2], gardener_id=row[3]) if row else None
    
    def delete(self):
        if self.id:
            CURSOR.execute("DELETE FROM plants WHERE id=?;", (self.id,))
            CONN.commit()
            print(f"plant {self.species} deleted.")
            self.id = None
        else:
            print("This plant is not in the database.")
    
    # Properties 
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, value,):
        if isinstance(value, str) and len(value) > 0:
            self._species = value
        else:
            raise ValueError("Species must not be empty.")
        
    @property 
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._height = value
        else:
            raise ValueError("Height must be a non-negative number")
        
    @property
    def gardener(self):
       from .gardener import Gardener
       return Gardener.find_by_id(self.gardener_id)

    # Instance methods 

    def info(self):
        return f"{self.species} - {self.height} in"
    
    def __repr__(self):
        return f"<Plant {self.id}: {self.species}, {self.height} in, Gardener {self.gardener_id}>"
    

