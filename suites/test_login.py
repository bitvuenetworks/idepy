import unittest
from selenium_core.selenium_ui_app import App

from ui_poms.ise.login_page import Login
from ui_poms.ise.administration.identity_management.users import Users
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

    def test_create_user(self):
        logger.info("Creating user")
        userPage = Users(self.app,logger)
        userPage.navigate_to_page()
        userPage.add_network_access_user("test123", "Demo@123", "Demo@123")
        time.sleep(2)
        logger.info("Done with user creation")

    def tearDown(self):
        logger.info("Closing the browser")
        # close the browser window
        # self.app.quit()

if __name__ == '__main__':
    unittest.main()
