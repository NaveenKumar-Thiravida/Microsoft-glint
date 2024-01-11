import configparser

config=configparser.RawConfigParser()
config.read("C:\Users\admin\PycharmProject\pythonProject\Microsoft-glint\Config\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('Common Data','baseURL')
        return url

    @staticmethod
    def getEmailAddress():
        email = config.get('Common Data', 'Email_address')
        return email

    @staticmethod
    def getClientID():
        client = config.get('Common Data', 'Client_id')
        return client

    @staticmethod
    def getPassword():
        password = config.get('Common Data', 'Password')
        return password
