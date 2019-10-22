import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _user_field = "UserName"
    _password_field = "Password"
    _login_button = "Login"

    def enterEmail(self, email):
        self.sendKeys(email, self._user_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def Login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("notifyAlert", locatorType="id")
        return result

    def verifyLoginFaild(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid User Name Or Password.')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("IvyCPG - Login")



