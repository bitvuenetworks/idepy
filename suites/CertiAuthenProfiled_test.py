import logging
import time
import unittest
from selenium_core.selenium_ui_app import App
from ui_poms.ise.workcenters.GuestAccess.ExtIdSources.Certifi_Authen_Profi import CertiAuthenProfi
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

    def test_create_user(self):
        logger.info("Creating Profile")
        userProfile = CertiAuthenProfi(self.app,logger)
        userProfile.navigate_to_page()
        userProfile.add_profile("BHANU", "PRAKASH")
        time.sleep(2)
        logger.info("Done with Profile creation")

    #def test_del_profile(self):
        logger.info("Deleting Profile")
        delprofile = CertiAuthenProfi(self.app, logger)
        #delprofile.navigate_to_page()
        delprofile.del_profile()
        time.sleep(3)
        logger.info("Done with deleting profile")


    def tearDown(self):
        logger.info("Closing the browser")
        # close the browser window
        # self.app.quit()

if __name__ == '__main__':
    unittest.main()
