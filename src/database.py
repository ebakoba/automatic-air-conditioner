import os
import sqlite3

DATABASE_PATH = os.path.join(os.getcwd(), 'database.sqlite3')

SWITCH_SQL = """
CREATE TABLE IF NOT EXISTS switch (
    last_switch INTEGER 
);
"""

class DataBase:
    def __init__(self):
        if not hasattr(self, 'connection'):
            self.connect_to_database()

    def connect_to_database(self):
        self.connection = sqlite3.connect(DATABASE_PATH)

    def database_setup(self):
        cursor = self.connection.cursor()
        cursor.execute(SWITCH_SQL)
        cursor.execute('SELECT COUNT(*) FROM switch')
        (number_of_rows,) = cursor.fetchone()
        print(number_of_rows)
        if number_of_rows < 1:
            cursor.execute('INSERT INTO switch (last_switch) VALUES (?)', (1,))
        self.connection.commit()
