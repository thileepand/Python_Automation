from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.select import Select

class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://qa-product-pg.ivycpg.com/web/DMS"
        #driver =  webdriver.Chrome(executable_path="/home/thileepan/Documents/driver/chromedriver")
        driverlocation = "/home/thileepan/Documents/driver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        username = driver.find_element(By.ID, "UserName")
        username.send_keys("png.admin")

        password = driver.find_element(By.ID, "Password")
        password.send_keys("1")

        loginbutton = driver.find_element(By.ID, "Login")
        loginbutton.click()

        time.sleep(3)

        clickmenu = driver.find_element(By.XPATH,
                                            "//ul[@id='collapsibleMenuContainer']//a[contains(text(),'Retailer Management')]")
        clickmenu.click()

        clickretailer = driver.find_element(By.XPATH,
                                            "//ul[@id='collapsibleMenuContainer']//a[contains(text(),'Retailer Master')]")
        clickretailer.click()
        time.sleep(2)

        driver.switch_to.frame("iContent")

        retailer = driver.find_element(By.XPATH, "//div[@id='mainContainer']//a[contains(text(),'Add')]")
        retailer.click()
        time.sleep(3)

        driver.quit()


ff = ClickAndSendKeys()
ff.test()