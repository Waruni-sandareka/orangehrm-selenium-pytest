import logging
from utilities.ReadConfig import ReadConfig

class LogGen:
    @staticmethod
    def loggen():
        log_path = ReadConfig.getLogPath()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        fileHandler = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        fileHandler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(fileHandler)

        return logger
