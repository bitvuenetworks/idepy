from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
from selenium.webdriver.common.by import By
from ui_poms.ise.Policy.Policy_Elements.Conditions.Conditions import Conditions

class Authentication(BasePage):
    """Base page class for Policy > Policy Elements > Conditions > Authentication
    """

    def __init__(self, app, logger):
        super(Authentication, self).__init__(app, logger)

    # overriden methods------------------------------------------------------

    def navigate_from_parent(self):
        """Overrides from BasePage"""
        self.navigate_authentication.click()

    def get_parent_page(self):
        """Overrides from BasePage"""
        return Conditions(self.app, self.logger)

    # navigation ui elements--------------------------------------------------

    @property
    def navigate_authentication(self):
        return Button(By.XPATH, "//a[@href='#collapseauthentication']", self.driver)
