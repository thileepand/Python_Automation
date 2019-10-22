import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #Locators
    _Login_Link = "Login"
    _email_Field = "user_email"
    _password_Field = "user_password"
    _Login_Button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._Login_Link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_Field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_Field)

    def clickLoginButton(self):
        self.elementClick(self._Login_Button, locatorType="name")

    def Login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), ' Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Lts's Kode It")

    def logout(self):
        self.nav.navigationToUserSettings()
        self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']", locatorType="xpath")
