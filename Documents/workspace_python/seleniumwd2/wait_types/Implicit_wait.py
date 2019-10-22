from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWait():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        username = driver.find_element(By.ID, "user_email")
        username.send_keys("thileepan88@gmail.com")
        password = driver.find_element(By.ID, "user_password")
       # login = driver.find_element(By.NAME, "commit")


ff = ImplicitWait()
ff.test()
