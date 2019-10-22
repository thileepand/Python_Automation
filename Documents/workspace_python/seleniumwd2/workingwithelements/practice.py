from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Practice():

    def test(self):

        baseURL = "https://www.airbnb.co.in/"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        driver.implicitly_wait(2)

        searchBox = driver.find_element(By.ID, "GeocompleteController-via-SearchBarLarge")
        searchBox.send_keys("chennai")

        Checkin = driver.find_element(By.ID, "startDate")
        Checkin.send_keys("23/04/2017")

        Checkout = driver.find_element(By.ID, "endDate")
        Checkout.send_keys("24/04/2017")

        dropdown = driver.find_element_by_class_name("GuestPickerTrigger__button")
        dropdown.click()
        time.sleep(2)

        # child = driver.find_element_by_class_name("button_j44uvu-o_O-button_1ndu018-o_O-button_small_plbzx7-o_O-button_light_497fkv")
        # child.click()
        # time.sleep(2)

        # search = driver.find_element_by_class_name("btn btn-primary btn-large btn-block")
        # search.click()
        # time.sleep(2)
        # driver.quit()




ff = Practice()
ff.test()


