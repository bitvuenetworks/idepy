from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import Link
from selenium_core.selenium_ui_elements import Input
from ui_poms.ise.administration.identity_management.identities import Identities
import time


class Users(BasePage):

    def __init__(self, app, logger):
        super(Users, self).__init__(app,logger)

    # navigation UI elements and actions -------------------------------------------------------------------------------

    @property
    def navigate_users(self):
        return Link(By.XPATH, "//a[@href='#administration/administration_identitymanagement/administration_identitymanagement_identities/users']", self.driver)

    def navigate_from_parent(self):
        self.navigate_users.click()

    def get_parent_page(self):
        return Identities(self.app, self.logger)

    # page UI elements -------------------------------------------------------------------------------------------------

    @property
    def users_add_button(self):
        return Button(By.ID, "addNacUserBtn", self.driver)


    # Edit Network Access User Form UI Elements-------------------------------------------------------------------------

    @property
    def network_access_user_name(self):
        return Input(By.ID, "nacUserName", self.driver)

    @property
    def network_access_user_password(self):
        return Input(By.ID, "nsfUserPwd", self.driver)

    @property
    def network_access_user_password_confirm(self):
        return Input(By.ID, "nsfUserPwd2", self.driver)

    @property
    def network_access_user_group_dropdown(self):
        return Button(By.XPATH, "//button[contains(@id,'xwt_widget_form_IconDropDownButton') and @wairole='button']",
                     self.driver)

    def network_access_user_group(self, user_group):
        return Button(By.XPATH, "//div[contains(text(),'"+user_group+"')]", self.driver)

    @property
    def submit_button(self):
        return Button(By.XPATH, "//button[@id='submitBtn']", self.driver)


    # page actions -----------------------------------------------------------------------------------------------------

    def add_network_access_user(self, name_text, password, password_confirm, user_group=None):
        """Adds a network access user
        :param name_text: the network user name
        :param password: the network user password
        :param password_confirm: the network user password re-entered
        """
        self.wait_for_loader([self.users_add_button])
        self.users_add_button.click()
        time.sleep(5)
        self.fill_network_access_user_form(name_text, password, password_confirm)
        time.sleep(10)
        if user_group is not None:
            self.network_access_user_group_dropdown.click()
            self.network_access_user_group(user_group).click()
        self.submit_button.scroll_to_element()
        self.submit_button.click()
        self.submit_button.click()

    #function to fill the form
    def fill_network_access_user_form(self, name_text, password, password_confirm):
        """Adds a network access user
        :param name_text: the network user name
        :param password: the network user password
        :param password_confirm: the network user password re-entered
        """
        self.wait_for_loader([self.network_access_user_name])

        self.network_access_user_name.click()
        self.network_access_user_name.send_text(name_text)

        self.network_access_user_password.click()
        self.network_access_user_password.send_text(password)

        self.network_access_user_password_confirm.click()
        self.network_access_user_password_confirm.send_text(password_confirm)


"""
if __name__ == "__main__":

    from .selenium_ui_app import App

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    ADMIN_USERNAME = 'username'
    ADMIN_PASSWORD = 'password'
    ISE_URL = "https://ISE_IP"
    SELENIUM_URL = "http://Selenium_IP:4444/wd/hub"

    app = App(SELENIUM_URL)
    login_page = Login(app, logger, ISE_URL)
    login_page.navigate_to_page()
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)

    page = Users(app, logger)
    page.navigate_to_page()
    page.add_network_access_user("test123", "Demo@123", "Demo@123")
"""
