import unittest
from selenium_core.selenium_ui_app import App
from ui_poms.ise.login_page import Login
from ui_poms.ise.Policy.Policy_Elements.Conditions.Authentication.Simple_Conditions import SimpleConditions
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
        page =Login(self.app, logger, ISE_URL)
        page.navigate_to_page()
        page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
        logger.info("Logged in.")

    def test_create_policy(self):
        logger.info("Creating_simple_condition_policy")
        policy_page = SimpleConditions(self.app,logger)
        policy_page.navigate_to_page()
        policy_page.add_simple_condition("krishna chaitanya reddy","ise server is over loaded")
        time.sleep(3)
        logger.info("deone with the policy creation")



if __name__=='__main__':
    unittest.main()
