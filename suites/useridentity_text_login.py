import logging
import time
import unittest
from selenium_core.selenium_ui_app import App
from ui_poms.ise.administration.identity_management.Groups.UserIdentity_Users import useridentity
from ui_poms.ise.login_page import Login

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


    def test_create_useridentity(self):
        logger.info("Creating the group")
        group = useridentity(self.app, logger)
        group.navigate_to_page()
        group.add_enter_group("Bitvue", "bitvue")
        time.sleep(5)
        logger.info("Done with creating a user identity group")