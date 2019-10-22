from selenium import webdriver

class FindByLinkText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path="/home/thileepan/Documents/driver/geckodriver")
        driver.get(baseUrl)

        elementByLinkText = ""

        if elementByLinkText is not None:
            print("We found an element by link text")

        elementByPartialLinkText = ""
        if elementByPartialLinkText is not None:
            print("We found an element by partial link text")

ff = FindByLinkText()
ff.test()