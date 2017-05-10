
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import CheckBox
from selenium.webdriver.common.by import By
from ui_poms.ise.Policy.Policy_Elements.results.authorization.authorization import Authorization
from selenium_core.selenium_ui_elements import *
import time


class AuthorizationProfile(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)


#Page UI Elements And Actions


    @property
    def navigate_authorization_policy(self):
        return Button(By.XPATH, "//div[contains(text(),'Authorization Profiles')]",  self.driver)

    def navigate_from_parent(self):
        self.navigate_authorization_policy.click()

    def get_parent_page(self):
        return Authorization(self.app,  self.logger)

# Page UIElements


    @property
    def authorization_profile_add_button(self):
        return Button(By.ID, "addProfileBtn",  self.driver)

    @property
    def authorization_profile_name(self):
        return Input(By.ID, "nsfProfileName",  self.driver)

    @property
    def authorization_profile_description(self):
        return Input(By.NAME, "nsfAuthZProfile.description",  self.driver)

    @property
    def authorization_profile_web_redirection(self):
        return Button(By.XPATH, ".//*[@id='WebAuthCheckbox']",  self.driver)

    @property
    def authorization_profile_acl(self):
        return Input(By.XPATH, "//tr[./td/span[contains(text(), 'ACL')]]/td/span/input[@type='text']" ,self.driver)


    @property
    def authorization_profile_value_dropdown(self):
        return Button(By.XPATH, "(//div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton'])[3]",self.driver)

    @property

    def authorization_profile_value_selection(self):
        return Button(By.XPATH, "//div[contains(text(),'my portal(chaitu)')]",  self.driver )

    @property
    def authorization_profile_submit_button(self):
        return Button(By.XPATH,  ".//span[contains(text(),'Submit')]",  self.driver)

    def add_authorization_profile(self,name,description,acl):
        self.wait_for_loader([self.authorization_profile_add_button])
        self.authorization_profile_add_button.click()
        time.sleep(3)



        self.fill_authorization_profile_form(name,description,acl)
        time.sleep(3)

        '''self.authorization_profile_web_redirection.scroll_to_element()
        self.authorization_profile_web_redirection.click()
        time.sleep(2)'''

        self.authorization_profile_value_dropdown.click()
        time.sleep(3)

        self.authorization_profile_value_selection.click()
        time.sleep(3)

        self.authorization_profile_submit_button.scroll_to_element()
        self.authorization_profile_submit_button.click()
        time.sleep(3)


    def fill_authorization_profile_form(self,name,description,acl):
        self.wait_for_loader([self.authorization_profile_name])

        self.authorization_profile_name.click()
        self.authorization_profile_name.send_text(name)
        time.sleep(3)

        self.authorization_profile_description.click()
        self.authorization_profile_description.send_text(description)
        time.sleep(3)

        self.authorization_profile_web_redirection.click()
        time.sleep(2)

        self.authorization_profile_acl.click()
        self.authorization_profile_acl.send_text(acl)
        time.sleep(3)