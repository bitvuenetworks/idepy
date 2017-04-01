from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Hover

class Workcenters(BasePage):

    def __init__(self,app,logger=None):
        super().__init__(app,logger)

        # navigation UI elements and actions -----------------------------------------------------------

    @property
    def navigate_workcenters(self):
        return Hover (By.XPATH, "//a[@data-item-id='workcenters']", self.driver)

    def navigate_from_parent(self):
        self.navigate_workcenters.hover()

    def get_parent_page(self):
        return None
