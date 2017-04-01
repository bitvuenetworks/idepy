from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.workcenters.workcenters import Workcenters
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Hover

class GuestAccess(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)


        # navigation UI elements and actions -------------------------------------------------------------------------------

    @property
    def navigate_guest_access(self):
        return Hover(By.XPATH,"//a[@href='#workcenters/workcenter_guest_access']" ,self.driver)


    def navigate_from_parent(self):
        self.navigate_guest_access.hover()

    def get_parent_page(self):
        return Workcenters(self.app,self.logger)

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

    page = GuestAccess(app, logger)
    page.navigate_to_page()
    time.sleep(5)
