from ui_poms.ise.administration.system.system import System
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
from selenium.webdriver.common.by import By


class  Settings(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    ###  PAGE UI ELEMENTS AND ACIONS  ###################

    @property
    def navigate_settings(self):
        return Button(By.XPATH,  "(//a[contains(text(),'Settings')])[1]", self.driver)

    def navigate_from_parent(self):
        self.navigate_settings.click()

    def get_parent_page(self):
        return System(self.app,   self.logger)


##########  PAGE UI ELEMENTS  ##########