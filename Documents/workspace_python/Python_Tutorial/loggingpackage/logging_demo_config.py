"""
Logger Demo
"""

import logging
import logging.config
from logging import FileHandler

class LoggerDemoConfig():

    def testlog(self):

        #create Logger
        logging.config.fileConfig("logging.config")
        logger = logging.getLogger(LoggerDemoConfig.__name__)

        #logging message
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")


ff = LoggerDemoConfig()
ff.testlog()