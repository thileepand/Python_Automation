from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from wait_types.explicit_wait_type import ExplicitWait


class ExpilicitWait():

    def test(self):
        baseURL = "http://www.expedia.com/"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplicitWait
        driver.get(baseURL)


        driver.find_element(By.ID, "tab-flight-tab").click()
        time.sleep(10)
        driver.find_element(By.ID, "flight-origin").send_keys("Ch")
        print("Ch is sended sucessfully")
        time.sleep(10)

        list1=driver.find_element(By.ID, "typeahead-list").find_elements(By.TAG_NAME,"li")
        list1[0].click()

        driver.find_element(By.ID, "flight-origin").send_keys("Mumbai")

        driver.find_element(By.ID, "flight-departing").send_keys("25/02/2017")
        returndate = driver.find_element(By.ID, "flight-returning")
        returndate.clear()
        returndate.send_keys("26/02/2017")
        driver.find_element(By.ID, "search-button").click()

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()


ff = ExpilicitWait()
ff.test()



