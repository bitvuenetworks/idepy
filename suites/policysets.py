import unittest
import time
import logging
from selenium_core.selenium_ui_app import App
from ui_poms.ise.login_page import Login
from ui_poms.ise.administration.system.settings.policy_sets.policy_sets_complete import PolicySetsComplete
from ui_poms.ise.Policy.policy_sets.complete_policy_sets import PolicySetsAuthenticationAndAutherizaton


logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
logger = logging.getLogger(__name__)


ADMIN_USERNAME = 'chaitu'
ADMIN_PASSWORD = 'Bitvue@123'
ISE_URL = "https://192.168.100.111"
SELENIUM_URL = "http://127.0.0.1:4444/wd/hub"

class FirstTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # create a new Firefox session
        logger.info("Into setup function")
        logger.info("Logging in.")

        self.app = App(SELENIUM_URL,browser='chrome')
        page = Login(self.app, logger, ISE_URL)
        page.navigate_to_page()
        page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
        logger.info("Logged in.")

    """
    def test_policy_sets_complete_enabl(self):
        logging.info(" policy sets enabling starts")
        enabling=PolicySetsComplete(self.app,logger)
        enabling.navigate_to_page()
        enabling.add_policy_sets_complete_enabling("chaitu", "Bitvue@123")
        logger.info(" policy sets enabled")
        time.sleep(2)"""



    def test_complete_policy_sets(self):
        logging.info(" adding policy sets for mobile divices(autherzation and auhentication policy)")
        policysets=PolicySetsAuthenticationAndAutherizaton(self.app,logger)
        policysets.navigate_to_page()
        policysets.add_policy_sets_authentication_and_autherization("mobile device"," moto, which new to market",
                                                                    "screen resolution","ram size",
                                                                    " camera quality"," wifi features",
                                                                    "bluetooth_adaptability")

        logger.info(" succfully added autherization and authentication for mobile device")
        time.sleep(1)

    @classmethod
    def tearDownClass(self):
        logger.info("closing the browser")

if __name__ == '__main__':
    unittest.main()

