from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingwithElementList():

    def test(self):

        baseURL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        driver.implicitly_wait(10)

        radioButtonList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonList)
        print("Size of the list "+str(size))

        for radioButton in radioButtonList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)


ff = WorkingwithElementList()
ff.test()

