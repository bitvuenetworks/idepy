from ui_poms.ise.workcenters.trestsec.components.components1 import Components
from selenium_core.selenium_ui_elements import *
from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By

class SecurityGroup(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    # Page UI elemens and actions

    @property
    def navigate_security_group(self):
        return Button(By.XPATH, "(//div[contains(text(),'Security Groups')])[1]", self.driver)

    def navigate_from_parent(self):
        self.navigate_security_group.click()

    def get_parent_page(self):
        return Components(self.app,  self.logger)


    ### PAGE ELEMENTS  #################

    @property
    def security_group_add_button(self):
        return Button(By.ID,  "SgtAddBtn",  self.driver)

    @property
    def security_group_name(self):
        return Input(By.ID,  "sgt.name",  self.driver)

    @property
    def security_group_description(self):
        return Input(By.XPATH,  "//textarea[@id='sgt.description']", self.driver)

    @property
    def security_group_propagete_to_acl_button(self):
        return Button(By.XPATH,  ".//*[@id='sgt.PropogateToApic']",self.driver)

    @property
    def security_group_submit_button(self):
        return Button(By.XPATH,  ".//*[@id='submitbtn']",self.driver)

    def add_security_group(self,name,description=None):
        self.wait_for_loader([self.security_group_add_button])
        self.security_group_add_button.click()
        time.sleep(3)

        self.fill_security_gruop_form(name,description)

        self.security_group_propagete_to_acl_button.click()
        time.sleep(3)

        self.security_group_submit_button.click()
        time.sleep(3)

    def fill_security_gruop_form(self,name,description):
        self.wait_for_loader([self.security_group_name])

        self.security_group_name.click()
        self.security_group_name.send_text(name)
        time.sleep(3)

        self.security_group_description.click()
        if description is None:
            self.security_group_description.send_text(description)
            time.sleep(3)