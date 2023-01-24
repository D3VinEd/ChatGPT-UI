import configparser

config = configparser.ConfigParser()
config.read("../config/config.ini")
print(config['OPENAI-API']['Engine'])
config.set('Test', 'test1', 'test1')
config.set('Test', 'test2', 'test2')
config.set('Test', 'test2', 'test5')
with open("../config/config.ini", 'w') as configfile:
    config.write(configfile)