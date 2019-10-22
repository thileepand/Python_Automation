"""
Logger Demo
"""

import logging

class LoggerDemoConsole():

    def testlog(self):

        #create Logger
        logger = logging.getLogger('sample_log')
        logger.setLevel(logging.INFO)

        #create console handler and set the level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #create formatter
        formatter = logging.Formatter("%(asctime)s- %(name)s- %(levelname)s: %(message)s:",
                            datefmt="%d/%m/%Y %I:%M:%S %p")
        #add formatter to console handler -> ch
        chandler.setFormatter(formatter)

        #add console handler to logger
        logger.addHandler(chandler)

        #logging message
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("crital message")

ff = LoggerDemoConsole()
ff.testlog()