from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTest(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://kelloggs-latam-qa.ivycpg.com/web/"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)
        lp = LoginPage(driver)
        lp.login("mex.division", "1")



        userIcon = driver.find_element(By.ID, "icons")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")
