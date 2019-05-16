from time import sleep
from src.configuration import ConfigurationService
from src.database import DataBase
from src.update import should_switch, update_time
from src.temperature import TemperatureService
from src.relayservice import RelayService

def start(database):
    database.database_setup()

def loop(configService, temperatureService, relayService):
    if should_switch():
        threshold = configService.get_config().threshold
        temperature = temperatureService.read_temperature()
        if threshold < temperature:
            relayService.switch(0)
        else:
            relayService.switch(1)

        update_time()
    sleep(2)

if __name__ == '__main__':
    database = DataBase()
    configService = ConfigurationService()
    temperatureService = TemperatureService(12)
    relayService = RelayService(16)
    start(database)
    while True:
        loop(configService, temperatureService, relayService)