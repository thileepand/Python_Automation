import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _retailer_master = "//ul[@id='collapsibleMenuContainer']//a[text()='Retailer Master']"
    _retailer_position_mapping = "//ul[@id='collapsibleMenuContainer']//a[text()='Retailer Position Mapping']"
    _route_master = "//ul[@id='collapsibleMenuContainer']//a[text()='Route']"
    _retailer_visit_plan = "//ul[@id='collapsibleMenuContainer']//a[text()='Retailer Visit Plan']"

    def NavigateToRetailerMaster(self):
        self.elementClick(locator=self._retailer_master, locatorType="xpath")

    def NavigateToRetailerPositionMapping(self):
        self.elementClick(locator=self._retailer_position_mapping, locatorType="xpath")

    def NavigateToRouteMaster(self):
        self.elementClick(locator=self._route_master, locatorType="xpath")

    def NavigateToRetailerVisitPlan(self):
        self.elementClick(locator=self._retailer_visit_plan, locatorType="xpath")




