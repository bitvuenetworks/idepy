from ui_poms.ise.administration.system.settings.policy_sets.policy_sets_complete import PolicySets
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *


class PolicySetsEnabling(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    @property
    def navigate_policy_sets_enabling(self):
        return Button(By.ID,  "policySetViewMode", self.driver)

    def navigate_from_parent(self):
        self.navigate_policy_sets_enabling.click()

    def get_parent_page(self):
        return PolicySets(self.app,  self.logger)

    #######PAGE UI ELEMENTS  ############



    @property
    def navigate_policy_sets_enabling_save_button(self):
        return Button(By.XPATH,  "(//*[contains(text(),'Save')])[1]", self.driver)

    def add_policy_sets_enabling(self):
        self.wait_for_loader([self.navigate_policy_sets_enabling_save_button])


        self.navigate_policy_sets_enabling_save_button.click()
        time.sleep(5)