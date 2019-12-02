import sqlite3

class db:
    def __init__(self, ab):
        self.conn = sqlite3.connect(ab)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS lista (id INTEGER PRIMARY KEY, tipus text, tevekenyseg text, mikor text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM lista")
        rows = self.cur.fetchall()
        return rows

    def insert(self, tipus, tevekenyseg, mikor):
        self.cur.execute("INSERT INTO lista VALUES(NULL, ?, ?, ?)", (tipus, tevekenyseg, mikor))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM lista WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, tipus, tevekenyseg, mikor):
        self.cur.execute("UPDATE lista SET tipus = ?, tevekenyseg = ?, mikor = ? WHERE id = ?", (tipus, tevekenyseg, mikor, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

database = db('lista.db')