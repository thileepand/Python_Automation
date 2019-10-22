from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _email_field ="SUA_Login_Id"
    _password_field = "SUA_Password"
    _Login_button = "Login"

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.ID, self._Login_button)

    def enterEmail(self, username):
        self.getEmailField().send_keys(username)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, username, password):
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()
