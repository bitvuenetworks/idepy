from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.workcenters.Guest_Access.Guest_Access import Guest_Access
from selenium_core.selenium_ui_elements import *

class Portals_Components(BasePage):
    def __init__(self,app,logger):
        super().__init__(app, logger)


        # navigation UI eliments and Basepage

    @property
    def navigate_Portals_Components(self):
        return Link(By.XPATH,".//*[@id='sub-navigation2']/div/ul/li[7]/a",self.driver)

    def navigate_from_parent(self):
        self.navigate_Portals_Components.click()

    def get_parent_page(self):
        return Guest_Access(self.app,self.logger)

