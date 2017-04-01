import unittest
from selenium_core.selenium_ui_app import App
from ui_poms.ise.login_page import Login
from ui_poms.ise.administration.identity_management.Groups.Endpoint_Groups import groups
import logging
import time

logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
logger = logging.getLogger(__name__)


ADMIN_USERNAME = 'bhanu'
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


    def test_create_groups(self):
        logger.info("Creating first_group")
        group = groups(self.app,logger)
        group.navigate_to_page()
        group.add_endpoint_indentity_groups("Prakash", "BHANU")
        time.sleep(5)
        logger.info("Done with Groups creation")

    """def test_create_second_group(self):
        logger.info("Creating group")
        group = groups(self.app,logger)
        group.navigate_to_page()
        group.add_endpoint_indentity_groups("Bitvue", "bhanu")
        time.sleep(2)
        logger.info("Done with Groups creation")"""

    def tearDown(self):
        logger.info("Closing the browser")
        # close the browser window
        # self.app.quit()

if __name__ == '__main__':
    unittest.main()