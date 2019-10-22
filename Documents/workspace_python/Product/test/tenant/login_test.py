import unittest
import pytest
from pages.tenant.login_page import LoginPage
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go the next verification point
    # If assert fails its stop current test execution and
    # Moves to next test method


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.Login("55555", "44444")
        result = self.lp.verifyLoginFaild()
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.Login("hdiv1", "2")  # 9894831103
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

