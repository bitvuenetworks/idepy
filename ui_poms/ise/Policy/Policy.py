from selenium_core.selenium_ui_app import App
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Hover
from selenium.webdriver.common.by import By


class Policy(BasePage):

    """Base page class for the Policy drop down on the home screen"""

    def __init__(self, app, logger):
        super(Policy, self).__init__(app, logger)

    # overriden methods------------------------------------------------------

    def navigate_from_parent(self):
        """Overrides from BasePage"""
        self.navigate_policy.hover()

    def get_parent_page(self):
        """Overrides from BasePage"""
        return None

    # navigation ui elements--------------------------------------------------

    @property
    def navigate_policy(self):
        return Hover(By.XPATH, "//a[@data-item-id='policy']", self.driver)


    # page UI elements -----------------------------------------------------------------------------


    # page actions ---------------------------------------------------------------------------------



