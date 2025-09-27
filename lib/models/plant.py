
from models import CURSOR, CONN

class Plant:
    def __init__(self, name, height, gardener_id, id=None):
        self.id = id
        self.name = name
        self.height = height  
        self.gardener_id = gardener_id

    # Properties
    @property
    def height(self):
        return f"{self._height} in"

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("Height must be an integer.")
        self._height = value

    # Class methods
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS plants (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            height INTEGER,
            gardener_id INTEGER,
            FOREIGN KEY(gardener_id) REFERENCES gardeners(id)
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS plants;"
        CURSOR.execute(sql)
        CONN.commit()

    # Others
    def save(self):
        if self.id:
            self.update()
        else:
            sql = "INSERT INTO plants (name, height, gardener_id) VALUES (?, ?, ?);"
            CURSOR.execute(sql, (self.name, self.height, self.gardener_id))
            CONN.commit()
            self.id = CURSOR.lastrowid

    def update(self):
        sql = "UPDATE plants SET name = ?, height = ?, gardener_id = ? WHERE id = ?;"
        CURSOR.execute(sql, (self.name, self.height, self.gardener_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM plants WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM plants;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls(id=row[0], name=row[1], height=row[2], gardener_id=row[3]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM plants WHERE id = ?;"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(id=row[0], name=row[1], height=row[2], gardener_id=row[3]) if row else None

    @classmethod
    def find_by_gardener(cls, gardener_id):
        sql = "SELECT * FROM plants WHERE gardener_id = ?;"
        rows = CURSOR.execute(sql, (gardener_id,)).fetchall()
        return [cls(id=row[0], name=row[1], height=row[2], gardener_id=row[3]) for row in rows]

    

