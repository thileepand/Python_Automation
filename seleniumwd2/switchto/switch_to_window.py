from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.implicitly_wait(10)
        driver.get(baseURL)

        #Find parent handle -> main window
        parenthandle = driver.current_window_handle
        print("parenthandle:" + parenthandle)

        #Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(3)

        #Find all handle there should be two handles after clicking open window button
        handles = driver.window_handles

        #Switch to window and search course
        for handle in handles:
            print("handle:" + handle)
            if handle not in parenthandle:
                driver.switch_to.window(handle)
                print("switched to window::" + handle)

                searchbox = driver.find_element(By.ID, "search-courses")
                searchbox.send_keys("python")
                time.sleep(3)
                driver.close()
                break

        #Switch back to the parent handle
        driver.switch_to.window(parenthandle)
        driver.find_element(By.ID, "name").send_keys("test")



ff = SwitchToWindow()
ff.test()
