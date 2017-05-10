import unittest
from selenium_core.selenium_ui_app import App
from ui_poms.ise.login_page import Login
from ui_poms.ise.administration.system.licensing.licensing import Licensing
import logging
from ui_poms.ise.administration.identity_management.groups.user_identity_groups.user_identity_groups import UserIdentityGroups
import time
from ui_poms.ise.administration.identity_management.identities.users.users import Users
from ui_poms.ise.administration.network_resourses.network_devices.network_devices import NetworkDevices
from ui_poms.ise.workcenters.Guest_Access.portals_components.guest_type.guest_type import GuestType
from ui_poms.ise.workcenters.Guest_Access.portals_components.guest_portal.Guest_Portal import GuestPortals
from ui_poms.ise.Policy.Policy_Elements.results.authorization.authorization_profiles.authorization_profiles import AuthorizationProfile
from ui_poms.ise.Policy.authorization.authorization import Authorization
from ui_poms.ise.Policy.Policy_Elements.results.client_provisioning.resources.resources import Resources


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

################gdfgdfgfdgdf##############


    """
    def test_enable_licensing(self):
       logger.info("enableing started")
       licensing_page=Licensing(self.app,logger)
       licensing_page.navigate_to_page()
       licensing_page.add_licensing_page()
       logger.info(" licence enabled:")



#########      user identity group creation     ############################################


    def test_creating_user_identity_group(self):
        logger.info("creating group started")
        group_page=UserIdentityGroups(self.app,logger)
        group_page.navigate_to_page()
        group_page.add_user_identity_group("(CHAITU) Guest Access Group",  "hi  every one i created this group for guest loggin .. please remember that every guest access user licence will be terminated after 90 days from the the day login")
        logger.info("group for our guests has been started please go on!")


# guest user creation#######################################


    def test_create_user(self):
       logger.info("Creating user")
       userPage = Users(self.app,logger)
       userPage.navigate_to_page()
       #users = [['test123','Demo@123','Demo@123'],['test1234','Demo1234@','Demo1234@']]
       #for i in range(len(users)):
       # userPage.add_network_access_user(users[i][0],users[i][1],users[i][2])

       userPage.add_network_access_user("chaitureddy", "chaitureddy518@gmail.com", "Chaitu@123", "Chaitu@123", "krishna","chaitanya reddy", "thanks for giving guest access")
        #time.sleep(3)

       # userPage.add_network_access_user("test123", "Demo@123", "Demo@123")
       time.sleep(2)
       logger.info("Done with user creation")




############    adding network device      #############################


    def test_network_device(self):
       logger.info(" adding network device to ise")
       device_page = NetworkDevices(self.app, logger)
       device_page.navigate_to_page()
       device_page.add_nework_device("Chaitu",  "please add as a private device ", "192.168.56.2", "toshiba", "c55-A")
       time.sleep(3)




##########         creating  Guest type           ##############


    def test_adding_guest_type(self):
       logger.info(" guest type creation started")
       guest_type  = GuestType(self.app,logger)
       guest_type.navigate_to_page()
       guest_type.add_guest_type("CHAITU",  " hi  i am just a 90 day dynamic guest user....","90")
       time.sleep(3)
       logger.info(" yhaaaaa u created guest type")


########           creating guest Portal         ####################


    def test_creat_guest_portal(self):
       logger.info(" guest poral creation started")
       guestportal=GuestPortals(self.app,logger)
       guestportal.navigate_to_page()
       guestportal.add_guest_portal("my portal(chaitu)","this is chaitu reddy")
       time.sleep(3)

       logger.info("guest portal creation completed")


#########          creting authorization profile(creating)       #########

    """
    def test_create_authorization_profile(self):
       logger.info("profile creation started")
       profile=AuthorizationProfile(self.app,logger)
       profile.navigate_to_page()
       profile.add_authorization_profile("Chaitu_krishna", "Authorized to chaitu only","dummy")
       time.sleep(5)
       logger.info("Authorization Profile is added")

#######     Authorization_profile(authorization)  ########

    """
    def test_authorization_profile(self):
       logger.info("reviewing the authorization")
       auth_profile=Authorization(self.app,logger)
       auth_profile.navigate_to_page()
       auth_profile.add_authorization(" developrs authorization(chaitu)")
       time.sleep(5)
       logger.info("  authorization is given success fully")
    
    
####  creating client provision  ############

    def test_client_privision(self):
        logger.info("client provision")
        resource=Resources(self.app,logger)
        resource.navigate_to_page()
        resource.add_resources_profile("windows CHAITU REDDY","i am but i won't","guestchaitu","https://www.cisco.com","192.168.100.118","22")
        time.sleep(3)
        logger.info("resource assigned")
    """
    @classmethod
    def tearDownClass(self):
        logger.info("closing the browser")

    if __name__ == '__main__':
        unittest.main()
