from db import Database

class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password
        self.id = None
        self.db = Database()

    def register(self):
        self.db.execute("SELECT * FROM users WHERE username = %s", (self.username,))
        if self.db.fetchone():
            print("Username already exists.")
        else:
            self.db.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (self.username, self.password)
            )
            print("Registration successful.")
        self.db.close()

    def login(self):
        self.db.execute(
            "SELECT id FROM users WHERE username = %s AND password = %s",
            (self.username, self.password)
        )
        result = self.db.fetchone()
        if result:
            self.id = result[0]
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False
