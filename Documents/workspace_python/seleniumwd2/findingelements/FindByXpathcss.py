from selenium import webdriver

class FindByXpathCss():
    def test(self):
        baseURL = "http://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.get(baseURL)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("we found element by Xpath")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByCss is not None:
            print("we found element by Css")


ff = FindByXpathCss()
ff.test()