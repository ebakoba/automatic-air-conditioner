from time import time
from database import DataBase

database = DataBase()

def should_switch():
    cursor = database.connection.cursor()
    cursor.execute("SELECT last_switch FROM switch")
    database_time = cursor.fetchone()[0]
    current_time = round(time())

    return (database_time + 60*60) < current_time


def update_time():
    cursor = database.connection.cursor()
    cursor.execute("UPDATE switch SET last_switch = ?", (round(time()),))
    database.connection.commit()
