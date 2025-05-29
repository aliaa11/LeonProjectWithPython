import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="loan_app",
            user="aliaa",
            password="aliaa123"
        )
        self.cur = self.conn.cursor()

    def execute(self, query, values=None, fetch=False):
        self.cur.execute(query, values or ())
        if fetch:
            return self.cur.fetchall()
        self.conn.commit()

    def fetchone(self):
        return self.cur.fetchone()

    def close(self):
        self.cur.close()
        self.conn.close()
