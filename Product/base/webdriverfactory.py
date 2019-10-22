"""
@package base

 WebDriver Factory class implementation
 It creates a web driver instance based on browser configurations

 Example:
     wdf = WebDriverFactory(browser)
     wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriver Factory class

        Returns:
            None

        """
        self.browser = browser
    """
        Set chrome driver and explorer environment based on OS

        chromedriver = "/hom/nadmin/Documents/driver/chromedriver"
        os.envision["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """
        # chromedriver = "/hom/nadmin/Documents/driver/chromedriver"
        # os.envision["webdriver.chrome.dirver"] = chromedriver
        # driver = webdriver.Chrome(chromedriver)

    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on the browser configuration

        Returns:
            'WebDriver Instance'

        """
        baseURL = "http://192.168.2.66/app1/DMS"
            # Set IE driver
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
            #Set chrome driver
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="/home/thileepan/Documents/driver/geckodriver")
        # elif self.browser == "chrome":
        #     chromedriver = "/home/thileepan/Documents/driver/chromedriver"
        #     os.environ["webdriver.chrome.driver"] = chromedriver
        #     driver = webdriver.Chrome(chromedriver)
        #     driver.set_window_size(1440, 900)
        #     driver.get(baseURL)
        else:
           driver = webdriver.Firefox(executable_path="/home/thileepan/Documents/driver/geckodriver")
           driver.get(baseURL)
           #driver = webdriver.Chrome(executable_path="/hom/nadmin/Documents/driver/chromedriver")
        #Setting Driver implicit time out for An Element
           driver.implicitly_wait(5)
        #Driver maximize window
           driver.maximize_window()
        #Loading browser with app URL
           #driver.get(baseURL)
        return driver
