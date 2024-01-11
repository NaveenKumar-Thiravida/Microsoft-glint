import logging

class LogGeneration:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=
                            'C:\\Users\\admin\\PycharmProject\\pythonProject\\Microsoft-glint\\Logs\\Automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %P')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger