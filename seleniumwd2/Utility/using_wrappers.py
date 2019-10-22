from selenium import webdriver
from selenium.webdriver.common.by import By
from Utility.Handywrappers import HandyWrappers
import time

class UsingWrappers():

    def test(self):

        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        hw = HandyWrappers(driver)
        driver.implicitly_wait(10)
        driver.get(baseURL)


        textField1 = hw.getElement("name")
        textField1.send_key("Test")
        time.sleep(3)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.Clear()



ff = UsingWrappers()
ff.test()
