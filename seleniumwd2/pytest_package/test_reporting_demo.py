import pytest
from pytest_package.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.abc = SomeClassToTest(40)

    def test_methodA(self):
        result = self.abc.sumNumbers(60, 30)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        result = self.abc.sumNumbers(20,25)
        assert result > 30
        print("Running method B")