import json
import threading
import os

CONFIG_PATH =  os.path.join(os.getcwd(), 'config.json')

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

class ConfigurationService:
    def __init__(self):
        if not hasattr(self, 'config'):
            self.read_config()
            set_interval(self.read_config, 10)

    def read_config(self):
        print('reading config')
        with open('config.json') as json_data_file:
            self.config = json.load(json_data_file)
            print(self.config)

    def get_config(self):
        return self.config

    #print(data)
    #threshold = data['threshold']
