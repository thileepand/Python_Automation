from selenium import webdriver

class FindByIdName():
    def test(self):
        baseURL = "http://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("we found element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("we found element by name")


ff = FindByIdName()
ff.test()