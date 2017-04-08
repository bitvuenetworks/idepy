from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Hover
from selenium_core.selenium_ui_elements import By

from ui_poms.ise.policy.policy import Policy



class PolicyElements(BasePage):
    """Base page class for the Policy Elements header under the Policy drop down on the main page
    The purpose of this is to keep a logical parent to "Dictionaries," "Conditions," and "Results"
    """

    def __init__(self, app, logger):
        super(PolicyElements, self).__init__(app, logger)

    # overriden methods------------------------------------------------------

    def navigate_from_parent(self):
        """Overrides from BasePage"""
        self.navigate_policy_elements.hover()

    def get_parent_page(self):
        """Overrides from BasePage"""
        return Policy(self.app, self.logger)

    # navigation ui elements--------------------------------------------------

    @property
    def navigate_policy_elements(self):
        return Hover(By.XPATH, "//a[@href='#policy/policy_elements']", self.driver)
