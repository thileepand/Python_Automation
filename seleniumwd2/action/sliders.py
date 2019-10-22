from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Sliders():

    def test(self):
        baseURL = "http://jqueryui.com/slider/"
        driverLocation = "/home/nadmin/Documents/driver/chromedriver"
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 150, 0).perform()
            print("Element slider successful")
            time.sleep(2)
        except:
            print("Element slider not successful")

ff = Sliders()
ff.test()
