from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpathFormat():

    def test(self):

        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        driver.get(baseURL)

        #Login lecture How to click and type on the web element
        driver.find_element(By.LINK_TEXT, "Login").click()
        emailfield  = driver.find_element(By.ID, "user_email")
        emailfield.send_keys("thileepan88@gmail.com")
        passwordfield = driver.find_element(By.ID, "user_password")
        passwordfield.send_keys("Thileepan@123")
        login = driver.find_element(By.NAME, "commit").click()

        #Search for course
        searchBox = driver.find_element(By.ID,"search-courses")
        searchBox.send_keys("Learn Python")

        #Select course
        _course = "//div[contains(@class, 'ourse-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("Learn Python 3 from scratch")

        courseElement = driver.find_element(By.XPATH,_courseLocator)
        courseElement.click()


ff = DynamicXpathFormat()
ff.test()
