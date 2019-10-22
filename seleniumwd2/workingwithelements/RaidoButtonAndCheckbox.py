from selenium import webdriver
import time

class RadioButton():

    def test(self):
        baseURL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        driver.implicitly_wait(3)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(3)
        bnzRadioBtn = driver.find_element_by_id("benzradio")
        bnzRadioBtn.click()

        time.sleep(3)
        bmwCheck = driver.find_element_by_id("bmwcheck")
        bmwCheck.click()

        time.sleep(3)
        bnzCheck = driver.find_element_by_id("benzcheck")
        bnzCheck.click()

        print("BMW Radio button is selected?" +str(bmwRadioBtn.is_selected())) # True is selected, False is not selected
        print("BENZ Radio button is selected?" + str(bnzRadioBtn.is_selected()))

        print("BMW Check box is selected?"+ str(bmwCheck.is_selected()))
        print("BENZ check obs is selected"+ str(bnzCheck.is_selected()))


ff = RadioButton()
ff.test()
