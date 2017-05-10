from ui_poms.ise.workcenters.trestsec.components.security_group.security_group1 import SecurityGroup
from selenium_core.selenium_ui_app import App
from ui_poms.ise.login_page import Login
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
import time
import unittest
import logging



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

    def test_security_group_creation(self):
        logging.info(" secrity group creation started")
        scg=SecurityGroup(self.app,logger)
        scg.navigate_to_page()
        scg.add_security_group("ChaituReddy",  " this is my trust stac:")
        time.sleep(3)
        logger.info(" SCG   creation completed:")

    def tearDown(self):
        logger.info("Closing the browser")
            # close the browser window
            # self.app.quit()

if __name__ == '__main__':
    unittest.main()

