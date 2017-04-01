from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
from ui_poms.ise.administration.identity_management.Identities.identity_management import IdentityManagement


class Groups(BasePage):
    def __init__(self, app, logger):
        super().__init__(app, logger)

    # navigation UI elements and actions -------------------------------------------------------------------------------

    @property
    def navigate_groups(self):
        return Link(By.XPATH,"//a[@href='#administration/administration_identitymanagement/administration_identitymanagement_groups']",self.driver)

    def navigate_from_parent(self):
        self.navigate_groups.click()

    def get_parent_page(self):
        return IdentityManagement(self.app, self.logger)
