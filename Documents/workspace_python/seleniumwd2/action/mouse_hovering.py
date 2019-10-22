from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MouseHovering():

    def test(self):
        baseURL = "https://kelloggs-latam-qa.ivycpg.com/web/"
        driverLocation = "/home/nadmin/Downloads/chromedriver"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)


        # driver.execute_script("window.scrollBy(0, 1000);")
        # time.sleep(3)
        # element = driver.find_element(By.ID, "mousehover")
        # itemToClickLocator = "//div[@class='mouse-hover-content']//a[text()='Top']"
        # try:
        #     actions = ActionChains(driver)
        #     actions.move_to_element(element).perform()
        #     print("Mouse Hovered on element")
        #     time.sleep(3)
        #     toplink = driver.find_element(By.XPATH, itemToClickLocator)
        #     actions.move_to_element(toplink).click().perform()
        #     print("Item Clicked")
        # except:
        #     print("Mouse hover failed on element")


        #driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        driver.find_element(By.ID, "SUA_Login_Id").send_keys("mex.division")
        driver.find_element(By.ID, "SUA_Password").send_keys("1")
        driver.find_element(By.ID, "Login").click()
        time.sleep(3)
        #element = driver.find_element(By.XPATH, "//li[@class='MainMenu']//a[text()='Masters']")
        element1 = driver.find_element(By.LINK_TEXT, "Masters")
        #element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Masters")))

        itemToClickLocator = "//li[@class='MenuLink']//a[text()='User Management']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element1).perform()
            print("Mouse Hovered on element")
            time.sleep(3)
            toplink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(toplink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse hover failed on element")

ff = MouseHovering()
ff.test()