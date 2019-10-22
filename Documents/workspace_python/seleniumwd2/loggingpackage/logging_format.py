"""
https://docs.python.org/3library/logging.html#logrecord-attributes
https://docs.python.org/3library/time.html#strftime
"""

import logging

logging.basicConfig(format= "%(asctime)s: %(levelname)s: %(message)s:",
                            datefmt="%d/%m/%Y %I:%M:%S %p",level=logging.DEBUG)
logging.warning("warning message")
logging.info("Info message")
logging.error("Error message")