from selenium_core.selenium_ui_app import App
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Keys
from selenium_core.selenium_ui_elements import By
from selenium_core.selenium_ui_elements import Hover


class Work_Centers(BasePage):

    def __init__(self, app, logger = None):
        super().__init__(app, logger)



#########          NAVIGATE TO WORK_CENTERS        ##########

    @property
    def navigate_work_centers(self):
        return Hover(By.XPATH, ".//*[@id='main-navigation']/li[6]/a", self.driver)

    def navigate_from_parent(self):
        self.navigate_work_centers.hover()

    def get_parent_page(self):
        return None
