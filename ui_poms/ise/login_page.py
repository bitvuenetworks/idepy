import time
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import Input
import logging
s_log = logging.getLogger()


class Login(BasePage):

    def __init__(self, app, logger=None, url=None):
        super().__init__(app)
        self.url = url

    # navigation UI elements and actions -------------------------------------------------------------------------------

    def navigate_to_page(self):
        s_log.info("Navigating to " + self.url + "...")
        self.driver.get(self.url)
        self.wait_for_loader(element_list=[self.username, self.password, self.login_button])

    def navigate_from_parent(self):
        s_log.info("This method is not applicable to Login Page. Doing nothing...")

    def get_parent_page(self):
        s_log.info("This method is not applicable to Login Page. Doing nothing...")

    # page UI elements -------------------------------------------------------------------------------------------------

    @property
    def username(self):
        return Input(By.ID, "dijit_form_TextBox_0", self.driver)

    @property
    def password(self):
        return Input(By.ID, "dijit_form_TextBox_1", self.driver)

    @property
    def identity_source_dropdown_button(self):
        return Button(By.ID, "authTypeId", self.driver)

    @property
    def login_button(self):
        return Button(By.ID, "loginPage_loginSubmit", self.driver)

    @property
    def next_button(self):
        return Button(By.ID, "carousel-next", self.driver)

    @property
    def maybe_later_button(self):
        return Button(By.XPATH, "//button[contains(text(),'Maybe later')]", self.driver)

    # page actions -----------------------------------------------------------------------------------------------------

    def login(self, username_text, password_text, timeout=20):
        """Performs login function as well as scrolling through initial pop-up dialogs
        :param username_text: the admin user's login
        :param password_text: the admin user's password
        """
        s_log.info("Filling in username and password fields")
        self.username.send_text(username_text, clear=True)
        self.password.send_text(password_text)

        s_log.info("Clicking login button")
        self.login_button.click()
        # self.login_button.send_text(Keys.RETURN)

        s_log.info("Handling initial pop-up dialogs...")
        while self.next_button.wait_for_element(timeout):
            self.next_button.click()
            time.sleep(1)  # allow dialog to perform sliding animation on UI
        if self.maybe_later_button.wait_for_element(timeout):
            self.maybe_later_button.click()
        time.sleep(2)
        s_log.info("Handled all pop-ups")
        s_log.info("Successfully logged into ISE UI")


if __name__ == "__main__":
    from selenium_core.selenium_ui_app import App

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
    logger = logging.getLogger(__name__)

    ADMIN_USERNAME = 'admin'
    ADMIN_PASSWORD = 'password'
    ISE_URL = "https://ISE_IP"
    SELENIUM_URL = "http://SELENIUM_IP:4444/wd/hub"

    app = App(SELENIUM_URL)
    page = Login(app,logger, ISE_URL)
    page.navigate_to_page()
    page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
