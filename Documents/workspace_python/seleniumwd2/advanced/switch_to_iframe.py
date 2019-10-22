from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToiFrame():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        driver.get(baseURL)
        driver.execute_script("window.scrollBy(0, 1500);")

        #Switch to frame using Id
        driver.switch_to.frame("courses-iframe")

        #Switch to frame using name
        #driver.switch_to.frame("courses-iframe")


        #Switch to frame using numbers
        #driver.switch_to.frame(0)


        time.sleep(5)
        #Search course
        searchVBox = driver.find_element(By.ID, "search-courses")
        searchVBox.send_keys("python")
        time.sleep(5)
        #Switch back to the parent handle
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1500);")
        time.sleep(5)

        driver.find_element(By.ID, "name").send_keys("Test Sucessful")


ff = SwitchToiFrame()
ff.test()