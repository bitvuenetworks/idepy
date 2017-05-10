from ui_poms.ise.Policy.Policy import Policy
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *


class Authorization(BasePage):
    def __init(self,app,logger):
        super(Authorization, self).__init__(app,logger)

    ##  Page  UI Elements And Actions


    @property
    def navigate_authorization(self):
        return Button(By.XPATH,  "//a[contains(@href,'#policy/policy_authorization')]",  self.driver)
                                #(dynamic xpath  (.//*[@id='main-navigation']/li[4]/ul/li[2]/ul[1]/li/a)

    def navigate_from_parent(self):
        self.navigate_authorization.click()

    def get_parent_page(self):
        return Policy(self.app,   self.logger)



#  Page UI Elements#######

    @property
    def drop_down_button(self):
        return Button(By.XPATH,  "(.//*[@title= 'Click to open menu'])[1]", self.logger)

    @property
    def drop_down_selection(self):
        return Button(By.XPATH,  "(.//td[contains(text(), 'Insert New Rule Above')])[3]", self.driver)

    @property
    def authorization_rule_name(self):
        return Input(By.XPATH,  "(//div[@class='dijit dijitReset dijitInlineTable dijitLeft xwtNotification cpmLocalPolicyNameTxtbox dijitTextBox xwtValidationTextBox'])[2]",  self.driver)

    @property
    def authorization_identity_group_condition_dropdown(self):
        return Button(By.XPATH,  "(.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[4]", self.driver)

    @property
    def authorization_identity_group_condition_dropdown_selecton(self):
        return  Button(By.XPATH,  "//button[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton']",self.driver)

    @property
    def authorization_selecting_user_identity(self):
        return Button(By.XPATH,  "//div[contains(text(),'User Identity Groups')]", self.driver)

    @property
    def authorizaion_user_identity_group_selection(self):
        return Button(By.XPATH,  "(.//div[@class='xwtObjectSelectorListText'])[12]",  self.driver)

    @property
    def authorization_permissions_dropdown(self):
        return Button(By.XPATH,  "(//span[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[6]", self.driver)

    @property

    def authorization_permission_dropdown_selection(self):
        return Button(By.XPATH,  "(//button[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2]",  self.driver)

    @property
    def authorization_security_group(self):
        return Button(By.XPATH,  "//div[contains(text(),'Security Group')]",  self.driver)

    @property
    def authorization_select_security_group(self):
        return Button(By.XPATH,  "//div[contains(text(),'Developers')]",  self.driver)

    @property
    def authorization_done(self):
        return Button(By.XPATH,  "(//a[contains(text(),'Done')])[2]", self.driver)

    @property
    def authorization_savebutton(self):
        return Button(By.ID,  "authzPolicySubmitBtn",  self.driver)

    def add_authorization(self,rule_name):
        self.wait_for_loader([self.drop_down_button])
        self.drop_down_button.click()
        time.sleep(3)

        self.drop_down_selection.click()
        time.sleep(3)

        self.fill_authorization_form(rule_name)
        time.sleep(3)

        self.authorization_identity_group_condition_dropdown.click()
        time.sleep(3)

        self.authorization_identity_group_condition_dropdown_selecton.click()
        time.sleep(3)

        self.authorization_selecting_user_identity.click()
        time.sleep(3)

        self.authorizaion_user_identity_group_selection.click()
        time.sleep(3)

        self.authorization_permissions_dropdown.click()
        time.sleep(3)

        self.authorization_permission_dropdown_selection.click()
        time.sleep(3)

        self.authorization_security_group.click()
        time.sleep(3)

        self.authorization_select_security_group.click()
        time.sleep(3)

        self.authorization_done.click()
        time.sleep(3)

        self.authorization_savebutton.click()
        time.sleep(3)

    def fill_authorization_form(self,rule_name):
         self.wait_for_loader([self.authorization_rule_name])
         self.authorization_rule_name.click()
         self.authorization_rule_name.send_text(rule_name)
