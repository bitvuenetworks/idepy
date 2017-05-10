from ui_poms.ise.administration.system.settings.settings import Settings
from selenium_core.selenium_ui_elements import *
from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By


class PolicySetsComplete(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    ###page UI Elements########################3

    @property
    def navigate_policy_sets(self):
        return Button(By.XPATH,  "(.//*[contains(text(),'Policy Sets')])[2]", self.driver)

    def navigate_from_parent(self):
        self.navigate_policy_sets.click()

    def get_parent_page(self):
        return Settings(self.app, self.logger)


    ##############3page elements and page acions######################

    @property
    def policy_sets_enabling(self):
        return Button(By.XPATH, ".//*[@id='policySetViewMode'] ", self.driver)

    @property
    def save_button(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Save')])[1]", self.driver)

    @property
    def  ok_popup(self):
        return Button(By.XPATH, " (.//*[contains(text(),'OK')])[2]", self.driver)


    ###############ofter logout here we are giving again username and passwd ###################

    @property
    def username(self):
        return Input(By.ID, "dijit_form_TextBox_0", self.driver)

    @property
    def password(self):
        return Input(By.ID, "dijit_form_TextBox_1", self.driver)

    ######## identity resourse button ################
    @property
    def identity_resourse_drop_down(self):
        return Button(By.XPATH, " .//*[@id='authTypeId']", self.driver)

    @property
    def selecting_internel(self):
        return Button(By.XPATH, " .//td[contains(text(), 'Internal')]", self.driver)

    @property
    def login_button(self):
        return Button(By.XPATH, ".//*[@id='loginPage_loginSubmit'] ", self.driver)

    def add_policy_sets_complete_enabling(self,username,password):
        self.wait_for_loader([self.policy_sets_enabling])
        self.policy_sets_enabling.click()
        time.sleep(5)


        self.save_button.click()
        time.sleep(5)

        self.ok_popup.click()
        time.sleep(5)

        self.fill_policy_sets_complete_enabling_form(username,password)
        time.sleep(5)


    def fill_policy_sets_complete_enabling_form(self,username,password):
        self.wait_for_loader([self.username])
        self.username.click()
        self.username.send_text(username)

        self.password.click()
        self.password.send_text(password)

       # self.identity_resourse_drop_down.click()
        #time.sleep(2)

        #self.selecting_internel.click()
        #time.sleep(4)

        self.login_button.click()
        time.sleep(8)



