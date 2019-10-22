from selenium import webdriver
import time

class WindowsSize():

    def test(self):

        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path= "/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        driver.get(baseURL)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height" + str(height))
        print("Width" + str(width))
        driver.quit()

ff = WindowsSize()
ff.test()