import pytest
from pytest_package.class_to_test import SomeClassToTest
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(50)

    def test_methodA(self):
        result = self.abc.sumNumbers(70,20)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")