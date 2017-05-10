from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import *
from selenium_core.selenium_ui_elements import Hover
from ui_poms.ise.Policy.Policy_Elements.results.results import Results


class Authorization(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    @property
    def navigate_authorization(self):
        return Button(By.XPATH,  ".//*[@id='headingpolicy_elements_permissions_authorization']/a",  self.driver)

    def navigate_from_parent(self):
        self.navigate_authorization.click()

    def get_parent_page(self):
        return Results(self.app,  self.logger)

