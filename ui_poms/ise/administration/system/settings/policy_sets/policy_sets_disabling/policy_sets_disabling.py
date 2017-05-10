from ui_poms.ise.administration.system.settings.policy_sets.policy_sets_complete import PolicySets
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *


class PolicySetsDisabling(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    @property
    def naviagte_policy_sets_disabling(self):
        return Button(By.ID, "//*[@id='simpleViewMode']",  self.driver)

    def navigate_from_parent(self):
        self.naviagte_policy_sets_disabling.click()

    def get_parent_page(self):
        return PolicySets(self.app,  self.logger)



    #######PAGE UI  ELEMENTS#################33

    def naviagte_policy_sets_disabling_save_button(self):
        return Button(By.XPATH,  "(//*[contains(text(),'Save')])[1]",  self.driver)

    def add_naviagte_policy_sets_disabling(self):
        self.wait_for_loader([self.naviagte_policy_sets_disabling_save_button()])

        self.naviagte_policy_sets_disabling_save_button().click()
        time.sleep(5)



