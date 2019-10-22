from selenium import webdriver

class BrowserInteraction():

    def test(self):
        baseURL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox(executable_path="/home/thileepan/Documents/driver/geckodriver")

        #Window maximize
        driver.maximize_window()

        #Open the URL
        driver.get(baseURL)

        #Get Title
        title = driver.title
        print("Title of the web page is: " + title)

        #Get the current URL
        currentUrl = driver.current_url
        print("Current URL of the web page is: "+ currentUrl)

        #Browser refresh
        driver.refresh()
        print("Browser refreshed first time: ")

        driver.get(driver.current_url)
        print("Browser refreshed second time: ")
        #Open another URl
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        driver.get(driver.current_url)
        print("Current URL of the web page is: " + currentUrl)
        #Browser back
        driver.back()
        print("Go one step back in browser history: ")

        #Browser forward
        driver.forward()
        print("Go one step forward in browser history")
        driver.get(driver.current_url)
        print("Current URL of the web page is: " + currentUrl)

        #Get page source
        pageSource = driver.page_source
        print(pageSource)

        #Browser close quite
        driver.quit()

ff = BrowserInteraction()
ff.test()
