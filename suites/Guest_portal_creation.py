import unittest
from selenium_core.selenium_ui_app import App

from ui_poms.ise.login_page import Login
from ui_poms.ise.administration.identity_management.users import Users
import logging
import time
from ui_poms.ise.workcenters.Guest_Access.Guest_Portals import Guest_Portals
from ui_poms.ise.workcenters.Guest_Access.Portals_Components import Portals_Components

import logging
import time


logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
logger = logging.getLogger(__name__)



ADMIN_USERNAME = 'chaitu'
ADMIN_PASSWORD = 'Bitvue@123'
ISE_URL = "https://192.168.100.111"
SELENIUM_URL = "http://127.0.0.1:4444/wd/hub"

class FirstTestCase(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        logger.info("Into setup function")
        logger.info("Logging in.")

        self.app = App(SELENIUM_URL,browser='chrome')
        page = Login(self.app, logger, ISE_URL)
        page.navigate_to_page()
        page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
        logger.info("Logged in.")


        self.guest_portal_creation = Guest_Portals(self.app,logger)

    def test_guest_portal_details(self):
        logger.info("creating Guest_Portal")
        Portal_Page=Guest_Portals(self.app,logger)
        Portal_Page.navigate_to_page()
        Portal_Page.add_guest_portal("chaitureddy","i am a new guest your my name is krishna chaiataya reddy")
        time.sleep(5)
        logger.info("Done with user creation")


    '''
    def tearDown(self):
            logger.info("Closing the browser")
            # close the browser window
            # self.app.quit()
    '''
if __name__ == '__main__':
    unittest.main()


