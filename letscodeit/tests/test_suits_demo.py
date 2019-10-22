import unittest

from tests.course.register_courses_csv_data import RegisterCourseCSVDataTests
from tests.home.login_test import LoginTest

#Get all the test from the test class
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCourseCSVDataTests)

#Create test suite combining all the test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)