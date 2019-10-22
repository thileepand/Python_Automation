from selenium import webdriver
import os

class RunChromeTests():
    #http: // chromedriver.storage.googleapis.com / index.html

    def testmethod(self):
        driverlocation = "/home/thileepan/Documents/driver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverlocation
        # Initiate the driver instance
        driver = webdriver.Chrome(driverlocation)
        # Open the URL
        driver.get("https://qa-product-pg.ivycpg.com/web/DMS")

ff = RunChromeTests()
ff.testmethod()
























