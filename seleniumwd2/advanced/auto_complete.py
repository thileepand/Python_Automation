from selenium import webdriver
import time

class AutoComplete:

    def test(self):
        baseURL = "https://www.southwest.com/"
        driverLocation = "/home/nadmin/Documents/driver/chromedriver"
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(baseURL)

        #send partial data
        cityField = driver.find_element_by_id("air-city-departure")
        cityField.send_keys("new york")
        time.sleep(5)

        #find the item to be click
        itemToselect = driver.find_element_by_xpath("//ul[@id='air-city-departure-menu']//li[contains(text(), 'NY - LGA')]")
        itemToselect.click()
        time.sleep(5)


ff = AutoComplete()
ff.test()