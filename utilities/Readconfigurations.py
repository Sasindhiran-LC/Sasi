from configparser import ConfigParser

def read_configuration(category,keys):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category,keys)