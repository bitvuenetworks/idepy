from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.Policy.Policy_Elements.Policy_Elements import PolicyElements
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import *
from selenium_core.selenium_ui_elements import Hover

class Results(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    @property
    def navigate_results(self):
        return Button(By.XPATH,  "//a[contains(text(),'Results')]",  self.driver)

    def navigate_from_parent(self):
        self.navigate_results.click()

    def get_parent_page(self):
        return PolicyElements(self.app,   self.logger)