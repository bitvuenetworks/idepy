from ui_poms.ise.administration.administration import Administration
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Hover
from selenium.webdriver.common.by import By




class System(BasePage):
    def __init__(self, app, logger):
        super().__init__(app, logger)

    @property
    def navigate_system(self):
        return Hover(By.XPATH, "//a[contains(@href,'administration/administration_system')]", self.driver)


    def navigate_from_parent(self):
        self.navigate_system.hover()


    def get_parent_page(self):
        return Administration(self.app,self.logger)
