from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.workcenters.Guest_Access.Guest_Access import GuestAccess
from selenium_core.selenium_ui_elements import *

class Portals_Components(BasePage):
    def __init__(self,app,logger):
        super().__init__(app, logger)


        # navigation UI eliments and Basepage

    @property
    def navigate_portals_components(self):
        return Link(By.XPATH,"//a[@href='#workcenters/workcenter_guest_access/workcenter_guest_access_configure']",self.driver)

    def navigate_from_parent(self):
        self.navigate_portals_components.click()

    def get_parent_page(self):
        return GuestAccess(self.app,self.logger)

if __name__ == '__main__':
    from selenium_core.selenium_ui_app import App
    from ui_poms.ise.login_page import Login
    import logging
    import time

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
    logger = logging.getLogger(__name__)

    ADMIN_USERNAME = 'chaitu'
    ADMIN_PASSWORD = 'Bitvue@123'
    ISE_URL = "https://192.168.100.111"
    SELENIUM_URL = "http://127.0.0.1:4444/wd/hub"

    app = App(SELENIUM_URL, browser='chrome')
    page = Login(app, logger, ISE_URL)
    page.navigate_to_page()
    page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    logger.info("Logged in.")

    page = Portals_Components(app, logger)
    page.navigate_to_page()
    time.sleep(2)


