from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
from selenium_core.selenium_ui_elements import By
from selenium_core.selenium_ui_elements import Input
from selenium_core.selenium_ui_elements import Link
from ui_poms.ise.administration.identity_management.Groups.groups import Groups


class useridentity(BasePage):

    def __init__(self, app, logger):
        super(useridentity, self).__init__(app, logger)


#######      NAVIGATE TO UI ELEMENTS      #########

    @property
    def navigate_useridentity(self):
        return Button(By.XPATH, "//span[contains(text(),'User Identity Groups')]",self.driver)

    def navigate_from_parent(self):
        self.navigate_useridentity.click()

    def get_parent_page(self):
        return Groups(self.app, self.logger)


#######     PAGE UI ELEMENTS       #########

    @property
    def add_useridentity_groupbutton(self):
        return Button(By.XPATH, ".//*[@id='addBtn']", self.driver)


    @property
    def enter_group_name(self):
        return Input(By.XPATH, ".//*[@id='nsfIdGroupName']", self.driver)


    @property
    def enter_group_description(self):
        return Input(By.XPATH, ".//*[@id='nsfIdGroup.description']", self.driver)


    @property
    def submit_group(self):
        return Button(By.XPATH, ".//*[@id='idGrpSubmitBtn']", self.driver)


#########      FUNCTIONS TO PAGE ACTIONS       ###########

    def add_enter_group(self, Name_text, Description):
        self.wait_for_loader([self.add_useridentity_groupbutton])
        self.add_useridentity_groupbutton.click()
        time.sleep(5)
        self.fill_enter_group_form(Name_text, Description)
        time.sleep(5)
        self.submit_group.click()
        time.sleep(7)


#########       FUNCTIONS TO FILL FORMS        ###########

    def fill_enter_group_form(self, Name_text, Description):

        self.wait_for_loader([self.enter_group_name])

        self.enter_group_name.click()
        self.enter_group_name.send_text(Name_text)

        self.enter_group_description.click()
        self.enter_group_description.send_text(Description)