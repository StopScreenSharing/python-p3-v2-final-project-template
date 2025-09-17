from . import CURSOR, CONN

class Gardener:
    all = []

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
        CURSOR.execute("INSERT INTO gardeners (name, phone) VALUES (?, ?)", (name, phone))
        CONN.commit()
        return cls(name, phone, CURSOR.lastrowid)

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM gardeners").fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]