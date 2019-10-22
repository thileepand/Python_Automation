import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class DivisionMasterPage(BasePage):

    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = "cc_field"
    _cc_exp = "cc-exp"
    _cc_cvv = "cc_cvc"
    _click_country = "country-select-inside"
    _select_country = "//select[@id='country-select-inside']/option[2]"
    _submit_enroll = "verify_cc_btn"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is invalid.')]"

    def enterCoursesName(self, name):
        self.sendKeys(name, locator=self._search_box)

    def selectCoursesToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNumber(self, num):
        self.sendKeys(num, locator=self._cc_num)

    def enterCardExp(self, exp):

        self.sendKeys(exp, locator=self._cc_exp)

    def enterCardCvv(self, cvv):
        self.sendKeys(cvv, locator=self._cc_cvv)

    #def clickCountry(self):
        #self.elementClick(locator=self._click_country, locatorType="id")

    #def selectCountry(self, country):
       # self.elementClick(locator=self._select_country, locatorType="xpath")

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll)

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNumber(num)
        self.enterCardExp(exp)
        self.enterCardCvv(cvv)
        #self.selectCountry(country)

    def enrollCourses(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message,locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
