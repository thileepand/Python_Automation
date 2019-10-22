from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseURL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox(executable_path="/home/thileepan /Documents/driver/geckodriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")




ff = ClickAndSendKeys()
ff.test()
