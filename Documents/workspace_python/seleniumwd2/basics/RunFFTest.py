from selenium import webdriver

class RunFFTests():

    def testmethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(executable_path="/home/thileepan/Documents/driver/geckodriver")
        #driver = webdriver.Firefox()
        # Open the URL
        driver.get("https://qa-product-pg.ivycpg.com/web/DMS")

ff = RunFFTests()
ff.testmethod()
























