from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Movie():

    def BookMovie(self):
        baseURL = "http://www.ticketnew.com/Movie-Ticket-Online-booking/C/Chennai"
        driver = webdriver.Chrome("/home/nadmin/Documents/driver/chromedriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        #driver.find_element(By.ID, "nav-link-theatres").click()
        driver.find_element_by_css_selector("#nav-link-theatres").click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//ul[@id='nav']//a[text()='Sangam Cinemas']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='divDates']//span[text()='6']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='faux-select-right png_bg']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id='faux-select-overlay-overflowed-content']//li[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='movie-name-list']//li[1]").click()
        driver.find_element(By.XPATH, "//table[@id='tblClassdetails']//tbody//tr[6]/td[5]/ul/li[1]/a").click()
        driver.find_element(By.ID, "s_1207").click()
        driver.find_element(By.XPATH, ".//div[@id='content-without-sidebar-container']//span[text()='Proceed to pay']").click()
        driver.find_element(By.XPATH, ".//ul[@id='alert-actions-large']//span[text()='I Accept']").click()
        driver.find_element(By.XPATH, "//*[@id='lnkskip']//span[text()='Skip food selection']").click()
        driver.find_element(By.ID, "txtemil").send_keys("test@test.com")
        driver.find_element(By.ID, "txtMobileNumber").send_keys("123456")
        driver.find_element(By.ID, "ChkTerms_1").click()
        time.sleep(2)
        driver.find_element(By.ID, "BtnPayment_1").click()
        time.sleep(5)
        driver.find_element_by_css_selector()

ch = Movie()
ch.BookMovie()