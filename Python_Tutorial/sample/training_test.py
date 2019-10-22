from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DistributorCreation():

    def test_distributor(self):
        baseURL = "https://qa.ivypay.in/web/PAY"
        driver = webdriver.Firefox(executable_path="/home/thileepan/Documents/driver/geckodriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(2)




        driver.find_element(By.ID, "inputEmail").send_keys("ivyadmin")
        driver.find_element(By.ID, "inputPassword").send_keys("1234")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Retailer Management").click()
        time.sleep(3)
        driver.switch_to.frame()
        mobileNo = driver.find_element(By.ID, "ARTR_IP_MobileNo")
        mobileNo.send_keys("7305673661")
        password = driver.find_element(By.ID, "ARTR_IP_Password")
        password.send_keys("test")
        print("keys sent")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 1000);")
        driver.find_element(By.ID, "Save").click()
       # time.sleep(3)


smoketest = DistributorCreation()
smoketest.test_distributor()


