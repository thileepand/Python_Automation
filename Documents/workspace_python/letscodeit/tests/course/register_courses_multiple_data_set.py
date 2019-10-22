from pages.courses.register_courses_page import RegisterCoursesPage
from selenium.webdriver.common.by import By
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCourseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "10", "12/12", "123"))#,("Learn Python 3 from scratch", "123456", "10/10", "888"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCoursesName(courseName)
        self.courses.selectCoursesToEnroll(courseName)
        self.courses.enrollCourses(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                     "Enrollment failed verification")
       # self.driver.find_element_by_link_text("All Courses").click().perform()
        self.driver.find_element(By.XPATH, "//div[@id='navbar']//img").click()
