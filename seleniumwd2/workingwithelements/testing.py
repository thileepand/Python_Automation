from selenium import webdriver
import time

class basic():

    def test(self):
        baseURL = "https://kelloggs-latam-qa.ivycpg.com/web/"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        driver.implicitly_wait(2)

        user = driver.find_element_by_id("SUA_Login_Id")
        user.send_keys("mex.division")

        pwd = driver.find_element_by_id("SUA_Password")
        pwd.send_keys("1")

        login = driver.find_element_by_id("Login")
        login.click()
        time.sleep(5)

ff = basic()
ff.test()
