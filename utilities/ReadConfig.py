import configparser

config = configparser.RawConfigParser()
config.read("configuration/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common_info', 'baseURL')

    @staticmethod
    def getUsername():
        return config.get('common_info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common_info', 'password')

    @staticmethod
    def getLogPath():
        return config.get('log', 'log_path')
