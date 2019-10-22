from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragAndDrop():

    def test(self):
        baseURL = "http://jqueryui.com/droppable/"
        driver = webdriver.Chrome(executable_path="/home/nadmin/Documents/driver/chromedriver")
        driver.implicitly_wait(6)
        driver.maximize_window()
        driver.get(baseURL)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        time.sleep(5)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(fromElement,toElement).perform()
            print("Drag and drop element successful")
            time.sleep(2)
        except:
            print("Drag and drop failed element")

ff = DragAndDrop()
ff.test()