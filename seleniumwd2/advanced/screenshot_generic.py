from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScreenShot():

    def test(self):
        baseURL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox(executable_path= "/home/thileepan/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        driver.get(baseURL)

        #Login link
        driver.find_element(By.LINK_TEXT, "Login").click()

        driver.find_element(By.ID, "user_email").send_keys("thileepan88@gmail.com")
        driver.find_element(By.ID, "user_password").send_keys("thileepan")
        driver.find_element(By.NAME, "commit").click()
        time.sleep(3)
        self.takeScreenshot(driver)


    def takeScreenshot(self, driver):
        """
        Take screen of the current open page
        :param driver:
        :return:
        """
        filename = str(round(time.time()* 1000)) + ".png"
        screenshotdirectory = "/home/thileepan/Documents//"
        destionationfile = screenshotdirectory + filename

        try:
            driver.save_screenshot(destionationfile)
            print("Screen shot saved to directory " + destionationfile)
        except NotADirectoryError:
            print("Not a directory error issue")


ff = ScreenShot()
ff.test()
