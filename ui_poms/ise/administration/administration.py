from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Hover


class Administration(BasePage):

    def __init__(self, app, logger=None):
        super().__init__(app, logger)

    # navigation UI elements and actions -----------------------------------------------------------

    @property
    def navigate_administration(self):
        return Hover(By.XPATH, "//a[@data-item-id='administration']", self.driver)

    def navigate_from_parent(self):
        self.navigate_administration.hover()

    def get_parent_page(self):
        return None

    # page UI elements -----------------------------------------------------------------------------

    # page actions ---------------------------------------------------------------------------------

