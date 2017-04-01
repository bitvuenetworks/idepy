from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import By
from ui_poms.ise.workcenters.work_centers import Work_Centers
from selenium_core.selenium_ui_elements import Hover


class Guest_Access(BasePage):

    def __init__(self, app, logger):
        super().__init__(app, logger)



#######     NAVIGATE TO GUEST_ACCESS        ##########

    @property

    def navigate_GuestAccess(self):
        return Hover(By.XPATH, ".//*[@id='main-navigation']/li[6]/ul/li[1]/ul[2]/li[1]/a", self.driver)

    def navigate_from_parent(self):
        self.navigate_GuestAccess.hover()


    def get_parent_page(self):
        return Work_Centers(self.app, self.logger)