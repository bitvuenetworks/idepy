from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
from ui_poms.ise.workcenters.GuestAccess.guest_access import Guest_Access


class ExtIdSources(BasePage):

    def __init__(self, app, logger):
        super().__init__(app, logger)



#########       NAVIGATE TO EXT_ID_SOURCES      ############

    @property

    def navigate_ext_id_sources(self):
        return Link(By.XPATH, ".//*[@id='main-navigation']/li[6]/ul/li[1]/ul[2]/li[5]/a", self.driver)

    def navigate_from_parent(self):
        self.navigate_ext_id_sources.click()

    def get_parent_page(self):
        return Guest_Access(self.app, self.logger)