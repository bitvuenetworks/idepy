import time
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import Input
from selenium_core.selenium_ui_elements import Link
from ui_poms.ise.administration.identity_management.Groups.groups import Groups


class groups(BasePage):

    def __init__(self, app, logger):
        super(groups, self).__init__(app,logger)


####### NAVIGATION TO UI ELEMENTS     #########

    @property
    def navigate_groups(self):
        return Link (By.LINK_TEXT, "Endpoint Identity Groups", self.driver)

    def navigate_from_parent(self):
        self.navigate_groups.click()

    def get_parent_page(self):
        return Groups(self.app, self.logger)


####### PAGE UI ELEMENTS #########

    @property
    def groups_add_button(self):
        return Button(By.XPATH, ".//*[@id='createBtn']", self.driver)


    @property
    def endpoint_identity_groups_Name(self):
        return Input(By.ID, "name", self.driver)

    @property
    def endpoint_identity_groups_Description(self):
        return Input(By.ID, "description", self.driver)

    @property
    def submit_button(self):
        return Button(By.ID, "submitbtn", self.driver)



########   FUNCTIONS TO PAGE ACTIONS   ##########

    def add_endpoint_indentity_groups(self, Name_text, Description):
        self.wait_for_loader([self.groups_add_button])
        self.groups_add_button.click()
        time.sleep(5)
        self.fill_endpoint_identity_groups_form(Name_text, Description)
        time.sleep(5)
        self.submit_button.click()
        time.sleep(5)



########   FUNCTIONS TO FILL GROUPS FORM   ##########

    def fill_endpoint_identity_groups_form(self, Name_text, Description):

        self.wait_for_loader([self.endpoint_identity_groups_Name])

        self.endpoint_identity_groups_Name.click()
        self.endpoint_identity_groups_Name.send_text(Name_text)

        self.endpoint_identity_groups_Description.click()
        self.endpoint_identity_groups_Description.send_text(Description)