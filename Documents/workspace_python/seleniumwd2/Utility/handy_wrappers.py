from selenium.webdriver.common.by import By

class HanyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID

        if locatorType == "name":
            return By.NAME

        if locatorType == "xpath":
            return  By.XPATH

        if locatorType == "css":
            return By.CSS_SELECTOR

        if locatorType == "classname":
            return  By.CLASS_NAME

        if locatorType =="linktext":
            return  By.LINK_TEXT

        else:
            print("locator" + locatorType + "not correct/supported")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found")
        except:
            print("Element not found")
        return element

    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False




