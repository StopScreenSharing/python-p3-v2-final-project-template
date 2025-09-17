
from . import CURSOR, CONN

class Plant:
    all = []

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
        """Insert a new plant into the database and return a Plant instance"""
        CURSOR.execute("""
            INSERT INTO plants (species, height, gardener_id)
            VALUES (?, ?, ?);
        """, (species, height, gardener_id))
        CONN.commit()

        new_id = CURSOR.lastrowid
        return cls(species, height, gardener_id, id = new_id)

    @classmethod
    def find_by_species(cls, species):
        return [plant for plant in cls.all if plant.species.lower() == species.lower()]
    
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
        return self._gardener
    
    @gardener.setter
    def gardener(self, value):
        from .gardener import Gardener
        if isinstance(value, Gardener):
            self._gardener = value
        else: 
            raise ValueError("Gardener must exist")

    # Instance methods 

    def info(self):
        return f"{self.species} - {self.height}cm"
    

