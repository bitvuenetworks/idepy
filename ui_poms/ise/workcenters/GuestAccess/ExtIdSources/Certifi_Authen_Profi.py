from selenium_core.selenium_ui_elements import *
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_app import App
from ui_poms.ise.workcenters.GuestAccess.ExtIdSources.Ext_Id_Sources import ExtIdSources
import time
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Keys

class CertiAuthenProfi(BasePage):

    def __init__(self, app, logger):
        super(CertiAuthenProfi, self).__init__(app, logger)


########        NAVIGATE TO  CERTIAUTHENPROFILED        ##########

    @property
    def navigate_certiauthenprofi(self):
        return Link(By.LINK_TEXT, "Certificate Authentication Profile", self.driver)

    def navigate_from_parent(self):
        self.navigate_certiauthenprofi.click()

    def get_parent_page(self):
        return ExtIdSources(self.app, self.driver)


########         NAVIGATING TO PAGE ELEMENTS        ############

    @property
    def profile_add_button(self):
        return Link(By.XPATH, ".//*[@id='CertProfileAddBtn']", self.driver)

    @property
    def profile_Name(self):
        return Input(By.XPATH, ".//*[@id='certificateAuthenProfileName']", self.driver)

    @property
    def profile_Description(self):
        return Input(By.XPATH, ".//*[@id='certificateAuthenProfileDescription']", self.driver)

    @property
    def submit_profile(self):
        return Link(By.XPATH, ".//*[@id='submitBtn']", self.driver)



#########       DELETING A CERTIFIED AUTHENTICATION PROFILE         ########


    @property
    def select_Profile_toDelete(self):
        return Button(By.XPATH, ".//*[@id='certificateAuthenProfileTable']/div[4]/div[2]/div[2]/div[1]/table/tbody/tr/td[1]/div/div",
                      self.driver)


    @property
    def delete_profile(self):
        return Link(By.XPATH, ".//*[@id='CertProfileDeleteBtn']", self.driver)

    @property
    def handle_popup(self):
        return Button(By.XPATH, "(//span[contains(text(), 'Delete')])[last()]", self.driver)


########        PAGE ACTIONS        ########

    def add_profile(self, Name_text, Description):
        self.wait_for_loader([self.profile_add_button])
        self.profile_add_button.click()
        time.sleep(5)
        self.fill_profile_form(Name_text, Description)
        time.sleep(5)
        self.submit_profile.click()
        time.sleep(3)

##########      TO DELETE PROFILE      #########
    def del_profile(self):
        self.select_Profile_toDelete.click()
        time.sleep(5)
        self.delete_profile.click()
        time.sleep(3)
        self.handle_popup.click()
        time.sleep(5)



    def fill_profile_form(self, Name_text, Description):

        self.wait_for_loader([self.profile_Name])

        self.profile_Name.click()
        self.profile_Name.send_text(Name_text)

        self.profile_Description.click()
        self.profile_Description.send_text(Description)