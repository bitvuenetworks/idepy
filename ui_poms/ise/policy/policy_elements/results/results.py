from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import By

from ui_poms.ise.policy.policy_elements.policy_elements import PolicyElements



class Results(BasePage):
    """Base page class for Policy > Policy Elements > Results
    """

    def __init__(self, app, logger):
        super(Results, self).__init__(app, logger)

    # overriden methods------------------------------------------------------

    def navigate_from_parent(self):
        """Overrides from BasePage"""
        self.navigate_results.click()

    def get_parent_page(self):
        """Overrides from BasePage"""
        return PolicyElements(self.app, self.logger)

    # navigation ui elements--------------------------------------------------

    @property
    def navigate_results(self):
        return Button(By.XPATH, "//a[@href='#policy/policy_elements/policy_elements_permissions']", self.driver)
