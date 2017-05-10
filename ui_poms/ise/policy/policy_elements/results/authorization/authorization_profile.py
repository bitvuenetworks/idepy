from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.policy.policy_elements.results.authorization.authorization import Authorization
from selenium_core.selenium_ui_elements import Link
from selenium_core.selenium_ui_elements import By
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import CheckBox
from selenium_core.selenium_ui_elements import Input
from selenium_core.selenium_ui_elements import SelectDropDown
from selenium_core.selenium_ui_elements import BaseElement
import time



class AuthorizationProfile(BasePage):

    def __init__(self, app, logger):
        super(AuthorizationProfile, self).__init__(app, logger)

    # overriden methods------------------------------------------------------

    def navigate_from_parent(self):
        """Overrides from BasePage"""
        self.navigate_authorization_profiles.click()

    def get_parent_page(self):
        """Overrides from BasePage"""
        return Authorization(self.app, self.logger)

    # navigation ui elements--------------------------------------------------

    @property
    def navigate_authorization_profiles(self):
        return Link(By.XPATH,
                    "//a[@href='#policy/policy_elements/policy_elements_permissions/policy_elements_permissions_authorization/policy_elements_permissions_authorization_authorization_profiles']",
                    self.driver)

    # page UI elements -------------------------------------------------------------------------------------------------

    @property
    def authorization_add_profile(self):
        return Button(By.ID, "addProfileBtn", self.driver)

    # edit UI elements -------------------------------------------------------------------------------------------------

    @property
    def authorization_profile_name(self):
        return Input(By.XPATH, "//input[@id='nsfProfileName']", self.driver)

    @property
    def authorization_profile_description(self):
        return Input(By.XPATH, "//textarea[@name='nsfAuthZProfile.description']", self.driver)

    @property
    def common_task_web_redirection_checkbox(self):
        return CheckBox(By.ID, "WebAuthCheckbox", self.driver)

    @property
    def web_redirection_dropdown(self):
        return Button(By.XPATH, "//span[text()[contains(.,'Centralized Web Auth')]]", self.driver)

    def client_provisioning(self):
        return Button(By.XPATH, "//td[text()[contains(.,'Client Provisioning')]]", self.driver).click()

    def hot_spot(self):
        return Button(By.XPATH, "//td[text()[contains(.,'Hot Spot')]]", self.driver).click()

    def mdm_redirect(self):
        return Button(By.XPATH, "//td[text()[contains(.,'MDM Redirect')]]", self.driver).click()

    def native_supplicant(self):
        return Button(By.XPATH, "//td[text()[contains(.,'Native Supplicant Provisioning')]]", self.driver).click()


    @property
    def web_redirection_acl(self):
        return Input(By.XPATH, "//tr[./td/span[contains(text(),'ACL')]]/td/span/input[@type='text']", self.driver)

    @property
    def web_redirection_value(self):
        return Input(By.ID, "cwaValueTypeValue", self.driver)

    @property
    def value_cp(self):
        return Button(By.XPATH, "//li[@id='cwaValueTypeValue_popup0']", self.driver)

    @property
    def acl(self):
        return CheckBox(By.ID, "ACLCheckbox",self.driver)


    @property
    def submit_button(self):
        return Button(By.XPATH, "//span[text()='Submit']", self.driver)

   # page actions -----------------------------------------------------------------------------------------------------

    def add_authorization_profile(self, name_text, description=None, portal_name=None, acl=None, redirection_value=None):
        """Adds a authorization profile
        :param name_text: the authorization profile name
        :param description: authorization profile description
        :param acl: Access Control List name
        :param redirection_value: value of the web direction
        """
        self.logger.info("Adding authorization profile {0}".format(name_text))
        #self.wait_for_loader([self.authorization_add_profile])
        time.sleep(5)
        self.authorization_add_profile.click()
        self.fill_authorization_profile_form(name_text, description, portal_name, acl, redirection_value)
        time.sleep(5)

    def fill_authorization_profile_form(self, name_text, description, portal_name, acl, redirection_value):
        """Fills out authorization profile form
        :param name_text: the policy set name
        :param description: the policy set description
        :param acl: Access Control List name
        :param ip_address: the ip address of the NAD

        """

        self.wait_for_loader([self.authorization_profile_name])

        time.sleep(5)
        self.authorization_profile_name.click()
        time.sleep(2)
        self.authorization_profile_name.send_text(name_text)
        time.sleep(2)
        self.authorization_profile_description.click()
        if description is not None:
            self.authorization_profile_description.send_text(description)

        if portal_name is not None:
            self.logger.info ("this is portal" + portal_name)
            self.common_task_web_redirection_checkbox.scroll_to_element()
            self.common_task_web_redirection_checkbox.click()
            time.sleep(3)
            if portal_name is not "Centralized Web Auth":
                self.logger.info("this is portal" + portal_name)
                self.web_redirection_dropdown.click()
                if portal_name == "Client Provisioning":
                    self.client_provisioning()
                elif portal_name == "Hot Spot":
                    self.hot_spot()
                elif portal_name == "MDM Redirect":
                    self.mdm_redirect()
                elif portal_name == "Native Supplicant Provisioning":
                    self.native_supplicant()
            time.sleep(3)
            self.web_redirection_acl.click()
            self.web_redirection_acl.send_text(acl)
            time.sleep(3)
            self.web_redirection_value.click()
            self.web_redirection_value.send_text(redirection_value)
            time.sleep(3)

            self.value_cp.click()
            time.sleep(2)

        time.sleep(3)
        self.wait_for_loader([self.submit_button])
        self.submit_button.click()
        time.sleep(10)


if __name__ == "__main__":

     from selenium_core.selenium_ui_app import App
     from ui_poms.ise.login_page import Login
     import logging

     logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
     logger = logging.getLogger(__name__)
     ADMIN_USERNAME = 'admin'
     ADMIN_PASSWORD = 'Asd@222'
     ISE_URL = "https://10.77.124.188/"
     SELENIUM_URL = "http://127.0.0.1:4444/wd/hub"

     app = App(SELENIUM_URL, "chrome")
     login_page = Login(app, logger, ISE_URL)
     login_page.navigate_to_page()
     login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)


     auth_prf = AuthorizationProfile(app, logger)
     auth_prf.navigate_to_page()
     logger.info("Adding new guest access profile")
     time.sleep(2)
     logger.info("Adding Wireless-dot1x-cpp profile")
     auth_prf.add_authorization_profile(name_text="Wireless-dot1x-cpp", portal_name="Client Provisioning", acl="initial",
                                        redirection_value="Client Provisioning Portal")
