from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FillTimeSheet():
    def timesheet(self):
        baseURL = "https://performancemanager10.successfactors.com/login?company=ivymobilit&loginMethod=PWD#/login"
        driverlocation = "/home/thileepan/Documents/driver/chromedriver"
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.get(baseURL)

        username = driver.find_element()





A = FillTimeSheet()
A.timesheet()