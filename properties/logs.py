"""
I suggest to create logger and all the parameters in one class.
"""

import logging as log
from datetime import datetime

from properties.config import TestData


class Logger:

    def __init__(self, name='Loger', log_level=log.DEBUG):
        self.logger = log.getLogger(Logger.__name__)
        self.logger.setLevel(log_level)
        time = datetime.now().strftime("%d-%m-%y %H.%M.%S")
        log_file = open(TestData.logging_dir + time + " " + name + ".log", 'a')
        log_file.write('-'*100 + '\n')
        fh = log.FileHandler(TestData.logging_dir + time + " " + name + ".log")
        formatter = log.Formatter('%(asctime)s :: %(module)s: %(funcName)s: %(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
