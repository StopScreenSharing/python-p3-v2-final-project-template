import sqlite3

CONN = sqlite3.connect('garden.db')
CURSOR = CONN.cursor()
