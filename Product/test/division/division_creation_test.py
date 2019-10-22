from pages.division.division_master import DivisionMasterPage
#from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCourseCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigationToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/hom/nadmin/Documents/workspace_python/letscodeit/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCoursesName(courseName)
        time.sleep(2)
        self.courses.selectCoursesToEnroll(courseName)
        time.sleep(2)
        self.courses.enrollCourses(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(2)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                     "Enrollment failed verification")