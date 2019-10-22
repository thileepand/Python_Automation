from selenium import webdriver
from selenium.webdriver.common.by import By
from Utility.handy_wrappers import HanyWrappers
import time

class ElementPrecentCheck():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        hw = HanyWrappers(driver)
        driver.get(baseURL)

        elementResult1 = hw.isElementPrecent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPrecensCheck("//input[@id='name1']", By.XPATH)
        print(elementResult2)


ff = ElementPrecentCheck()
ff.test()