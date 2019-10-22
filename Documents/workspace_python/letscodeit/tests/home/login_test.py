from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go the next verification point
    # If assert fails its stop current test execution and
    # Moves to next test method

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.Login("thileepan88@gmail.com", "Thileepan@123")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validlogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.Login("thileepan88@gmail.com", "abc")
        result = self.lp.verifyLoginFailed()
        time.sleep(3)
        assert result == True

    # @pytest.mark.run(order=2)
    # def test_invalidLogin(self):
    #     self.lp.Login("thileepan88@gmail.com", "")
    #     time.sleep(3)
    #     result = self.lp.verifyLoginFailed()
    #     assert result == True

    # @pytest.mark.run(order=3)
    # def test_invalidLogin(self):
    #     self.lp.Login("", "Thileepan@123")
    #     result = self.lp.verifyLoginFailed()
    #     time.sleep(3)
    #     assert result == True

