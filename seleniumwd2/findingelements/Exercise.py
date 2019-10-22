from selenium import webdriver

class Exercise():

    def test(self):

        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.maximize_window()
        baseURL = 'https://letskodeit.teachable.com/p/practice'
        title = driver.title
        driver.get(baseURL)

        print(title)

ff = Exercise()
ff.test()