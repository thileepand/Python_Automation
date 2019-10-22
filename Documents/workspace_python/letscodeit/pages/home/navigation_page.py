import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _my_courses = "My Courses"
    _all_courses = "//div[@id='navbar']//div/img"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//span[text()='User Settings']"

    def navigationToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def navigationToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigationToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigationToUserSettings(self):
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")

