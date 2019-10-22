import pytest
from pytest_package.class_to_test import SomeClassToTest
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(70,20)
        assert result == 135
        print("Running method A")

    def test_methodB(self):
        print("Running method B")