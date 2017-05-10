from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
#from selenium_core.selenium_ui_elements import Hover
from selenium.webdriver.common.by import By
from ui_poms.ise.Policy.Policy_Elements.Policy_Elements import PolicyElements


class Conditions(BasePage):
    """Base page class for Policy > Policy Elements > Conditions
    """
    def __init__(self, app, logger):
        super(Conditions, self).__init__(app, logger)

    # overriden methods------------------------------------------------------

    def navigate_from_parent(self):
        """Overrides from BasePage"""
        self.navigate_conditions.click()

    def get_parent_page(self):
        """Overrides from BasePage"""
        return PolicyElements(self.app, self.logger)

    # navigation ui elements--------------------------------------------------

    @property
    def navigate_conditions(self):
        return Button(By.XPATH, "//a[@href='#policy/policy_elements/policy_elements_conditions']", self.driver)
