from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollElement():

    def test(self0):
        baseURL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox(executable_path= "/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        driver.get(baseURL)


        #Scroll down
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)

        #Scroll up
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)

        #Scroll element into view
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150);")

        #Native way to scroll element into view
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print("Location:" + str(location))
        driver.execute_script("window.scrollBy(0, -150);")


ff= ScrollElement()
ff.test()



