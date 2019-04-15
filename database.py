import os
import sqlite3

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

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