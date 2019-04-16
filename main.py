from time import sleep
from src.database import DataBase
from src.update import should_switch, update_time

database = DataBase()

def start():
    database.database_setup()

def loop():
    print(should_switch())
    if should_switch():
        # do logic here
        update_time()
    sleep(2)

start()
while True:
    loop()