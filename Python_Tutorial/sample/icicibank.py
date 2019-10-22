from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class LoginPage():

    def Login_Link(self):
        baseURL = "https://www.icicibank.com/"
       # driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver = webdriver.Chrome("/home/nadmin/Documents/driver/chromedriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(2)

        Login = driver.find_element(By.XPATH, "//div[@id='main']//a[@title='Internet Banking Login']")
        #Login.click()

        personalLogin =  "//div[@id='IBLogin-child']//ul[1]//a[contains(text(),'Personal, NRI and Young Stars')]"
        #personalLogin.click()


        try:
            actions = ActionChains(driver)
            actions.move_to_element(Login).perform()
            print("Mouse hovered on element")
            time.sleep(2)
            LoginLink = driver.find_element(By.XPATH, personalLogin)
            actions.move_to_element(LoginLink).click().perform()
            print("Item clicked")
            time.sleep(5)
        except:
            print("Element not found")

        text = driver.find_element(By.XPATH,
                                       "//div[@class='primier_banners desktop-only clearfix']//a[contains(text(),'Continue to Login')]")
        text.click()
        time.sleep(5)

a = LoginPage()
a.Login_Link()