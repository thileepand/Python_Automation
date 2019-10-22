from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class HiddenElements():

    def test(self):
        baseURL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        driver.implicitly_wait(10)

        # Find the state of the text box
        textboxelement = driver.find_element_by_id("displayed-text")
        textboxstate = textboxelement.is_displayed() #True is visible, False if hidden
        #Exception if not present in the DOM
        print("Text is visible? " + str(textboxstate))
        time.sleep(2)

        #Click the hidden button
        driver.find_element_by_id("hide-textbox").click()

        # Find the state of the text box
        textboxstate = textboxelement.is_displayed()  # True is visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textboxstate))
        time.sleep(2)

        #Click on the show button
        driver.find_element_by_id("show-textbox").click()
        #Find the state of the text box
        textboxstate = textboxelement.is_displayed()
        print("Text is visible? " + str(textboxstate))
        time.sleep(2)
        #Browser close
        driver.quit()

    def test1(self0):
        baseURL = 'http://www.expedia.com'
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        driver.implicitly_wait(10)

        driver.find_element_by_id("tab-flight-tab").click()

        element = driver.find_element_by_id("flight-children")
        sel = Select(element)
        sel.select_by_index("2")
        time.sleep(2)

        dropdownelement = driver.find_element_by_id("flight-age-select-1") # True is visible, False if hidden
        sel1 = Select(dropdownelement)
        sel1.select_by_index("3")
        time.sleep(3)
        #print("dropdownelement visibile" + str(dropdownelement.is_displayed()))
        driver.quit()


ff = HiddenElements()
ff.test()
ff.test1()