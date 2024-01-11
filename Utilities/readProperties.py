import configparser

config=configparser.RawConfigParser()
config.read('C:\\Users\\admin\\PycharmProject\\pythonProject\\Microsoft-glint\\Config\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common','url')
        return url

    @staticmethod
    def getEmailAddress():
        email = config.get('common', 'email_address')
        return email

    @staticmethod
    def getClientID():
        client = config.get('common', 'client_id')
        return client

    @staticmethod
    def getPassword():
        password = config.get('common', 'password')
        return password
