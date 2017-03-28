from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.workcenters.workcenters import Work_Centers
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Hover

class Guest_Access(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)


        # navigation UI elements and actions -------------------------------------------------------------------------------

    @property
    def navigate_Guest_Access(self):
        return Hover(By.XPATH,".//*[@id='main-navigation']/li[6]/ul/li[1]/ul[2]/li[1]/a",self.driver)


    def navigate_from_parent(self):
        self.navigate_Guest_Access.hover()

    def get_parent_page(self):
        return Guest_Access(self.app,self.logger)