from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class DropDownElement():

    def test(self):

        baseURL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)


        sel.select_by_value("benz")
        print("select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("select BMW by visual text")
        time.sleep(2)

        sel.select_by_index(2)
        print("select Honda by index")

ff = DropDownElement()
ff.test()

