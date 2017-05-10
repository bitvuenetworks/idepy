from ui_poms.ise.administration.administration import Administration
from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Hover

class NetworkResourses(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    #Page ui Elements And Actions

    @property
    def navigate_network_resourses(self):
        return Hover(By.XPATH, "//a[@href='#administration/administration_networkresources']",  self.driver)

    def navigate_from_parent(self):
        self.navigate_network_resourses.hover()

    def get_parent_page(self):
        return Administration(self.app,   self.logger)