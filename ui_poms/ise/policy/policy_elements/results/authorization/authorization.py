from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import By
from ui_poms.ise.policy.policy_elements.results.results import Results
import time



class Authorization(BasePage):
    """Base page class for Policy > Policy Elements > Results > Authorization
    """

    def __init__(self, app, logger):
        super(Authorization, self).__init__(app, logger)

    # overriden methods------------------------------------------------------

    def navigate_from_parent(self):
        """Overrides from BasePage"""
        time.sleep(5)
        self.navigate_authorization.click()

    def get_parent_page(self):
        """Overrides from BasePage"""
        return Results(self.app, self.logger)

    # navigation ui elements--------------------------------------------------

    @property
    def navigate_authorization(self):
        return Button(By.XPATH, "//a[@href='#collapsepolicy_elements_permissions_authorization']", self.driver)
