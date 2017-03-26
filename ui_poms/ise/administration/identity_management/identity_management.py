from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.administration.administration import Administration
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Hover


class IdentityManagement(BasePage):

    def __init__(self, app, logger):
        super().__init__(app, logger)

    # navigation UI elements and actions -------------------------------------------------------------------------------

    @property
    def navigate_identity_management(self):
        return Hover(By.XPATH, "//a[@href='#administration/administration_identitymanagement']", self.driver)

    def navigate_from_parent(self):
        self.navigate_identity_management.hover()

    def get_parent_page(self):
        return Administration(self.app, self.logger)

    # page UI elements -------------------------------------------------------------------------------------------------

    # page actions -----------------------------------------------------------------------------------------------------
