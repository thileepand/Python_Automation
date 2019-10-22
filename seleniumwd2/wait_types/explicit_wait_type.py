from traceback import print_stack
from Utility.handy_wrappers import HanyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWait():

    def __init__(self, driver):
        self.driver = driver
        self.hw = HanyWrappers(driver)


    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):

        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  "::seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            stop = wait.until(EC.element_to_be_clickable((byType,
                                                          "stopFilter_stops-0")))

            print("Element appeared on the webpage")
        except:
            print("Element not appeared on the webpage")
            print_stack()
        return element
