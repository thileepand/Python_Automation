from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test(self):
        baseURL = 'https://www.expedia.com'
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        driver.get(baseURL)

        #Click on flight tab
        driver.find_element_by_id("tab-flight-tab").click()

        #Find departing field
        departingField = driver.find_element_by_id("flight-departing")

        #Click departing field
        departingField.click()

        #Select departing date
        dateToselct = driver.find_element(By.XPATH,
                                          "//caption[text()='FEB 2017']/ancestor::table[1]/tbody[@class='datepicker-cal-dates']/tr[5]/td[1]/button[text()='27']")
        dateToselct.click()
        #Click the date

        time.sleep(5)
        driver.quit()


    def test2(self):
        baseURL = 'https://www.expedia.com'
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        driver.get(baseURL)

        # Click on flight tab
        driver.find_element_by_id("tab-flight-tab").click()

        # Find departing field
        departingField = driver.find_element_by_id("flight-departing")

        # Click departing field
        departingField.click()

        #Select the date
        dateToselect = driver.find_element(By.XPATH,
                                               "//caption[text()='FEB 2017']/ancestor::table[1]/tbody[@class='datepicker-cal-dates']/tr[5]")
        validdate = dateToselect.find_element(By.TAG_NAME, "td")

        time.sleep(5)

        for date in validdate:
            if date.text== "27":
                date.click()
                break

ff = CalendarSelection()
ff.test2()

