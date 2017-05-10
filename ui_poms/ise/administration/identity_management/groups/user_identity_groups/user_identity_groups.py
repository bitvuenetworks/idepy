from ui_poms.ise.administration.identity_management.groups.groups import Groups
from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import Link
from selenium_core.selenium_ui_elements import Input
import time


class UserIdentityGroups(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    #page ui elements and actions


    @property
    def navgate_user_identity_group(self):
        return Button(By.XPATH,  "//span[contains(text(),'User Identity Groups')]", self.driver)

    def navigate_from_parent(self):
        self.navgate_user_identity_group.click()

    def get_parent_page(self):
        return Groups(self.app, self.driver)


    #Page UI Elements
#user identity group add button
    @property
    def group_add_button(self):
        return Button(By.XPATH, "//button[@id='addBtn']",self.driver)

#group name

    @property
    def group_name(self):
        return Input(By.XPATH, "//input[@id='nsfIdGroupName']", self.driver)

#group description

    @property
    def group_description(self):
        return Input(By.XPATH, "//textarea[@id='nsfIdGroup.description']", self.driver)

#submit button

    @property
    def submit_button(self):
        return Button(By.XPATH, "//button[@id='idGrpSubmitBtn']", self.driver)

### page actions#######################

    def add_user_identity_group(self,name,description=None):

        self.wait_for_loader([self.group_add_button])
        self.group_add_button.click()
        time.sleep(5)

        self.fill_user_identity_group_form(name,description)
        time.sleep(12)

        self.submit_button.click()
        time.sleep(5)

#filling the form

    def fill_user_identity_group_form(self,name,description):
        self.wait_for_loader([self.group_name])
        self.group_name.click()
        self.group_name.send_text(name)
        time.sleep(2)

        self.group_description.click()
        self.group_description.send_text(description)
        time.sleep(3)
