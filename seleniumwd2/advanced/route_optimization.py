from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class ScreenShot():

    def test(self):
        baseURL = 'http://192.168.2.21/app1'
        driver = webdriver.Chrome(executable_path= "/home/thileepan/Documents/driver/chromedriver")
        driver.implicitly_wait(2)
        driver.get(baseURL)
        driver.maximize_window()
        #Login link
        uploadElement = driver.find_element(By.ID, "InputFile")
        # uploadElement.click()
        uploadElement.send_keys("/home/thileepan/Documents/Bangalore_Retailers.xlsx")
        driver.find_element(By.ID, "btnFileUpload").click()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 1500);")
        time.sleep(3)
        driver.find_element(By.ID, "inputCluster").clear()
        driver.find_element(By.ID, "inputCluster").send_keys("6")
       # Cluster.send_keys("5")
        driver.find_element(By.ID, "btnGetRefreshedCluster").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//tr[@id='3']//td[1]").click()
        driver.find_element(By.ID, "btnESRICall").click()
        time.sleep(3)
        driver.find_element(By.ID, "btnGetSellerList").click()
        # time.sleep(3)
        # element  = driver.find_element(By.ID, "selectedDD")
        # sel = Select(element)
        # sel.select_by_index("1")
        time.sleep(10)

        self.takeScreenshot(driver)


    def takeScreenshot(self, driver):
        """
        Take screen of the current open page
        :param driver:
        :return:
        """
        filename = str(round(time.time()* 1000)) + ".png"
        screenshotdirectory = "/home/thileepan/Documents/ScreenShot//"
        destionationfile = screenshotdirectory + filename

        try:
            driver.save_screenshot(destionationfile)
            print("Screen shot saved to directory " + destionationfile)
        except NotADirectoryError:
            print("Not a directory error issue")


ff = ScreenShot()
ff.test()
