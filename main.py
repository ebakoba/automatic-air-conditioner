from time import sleep
from database import DataBase

database = DataBase()

def start():
    database.database_setup()

def loop():
    sleep(2)

start()
while True:
    loop()