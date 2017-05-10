import unittest
from selenium_core.selenium_ui_app import App
from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.workcenters.Device_Administration.Identities.Users.Users import Users
from ui_poms.ise.login_page import Login
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
        logger.info("creatig user")
        userpage=Users(self.app,logger)
        userpage.navigate_to_page()
        userpage.add_network_access_user("REDDY", "chaitureddy.1994@gmail.com", "Chaitu@1994" , "Chaitu@1994",
                                         "krishna", "chaitanya reddy", "i am  new but known")

        time.sleep(5)

        logger.info(" haa ha i hit you")
#deletion started

        logger.info("i am killing you .....")

        delpage=Users(self.app,logger)
        delpage.delete_user()
        time.sleep(8)
        logger.info("sorry love! you are terminated!    see u next gen")

    def tearDown(self):
        logger.info("closing the browser")

if __name__ == '__main__':
        unittest.main()

