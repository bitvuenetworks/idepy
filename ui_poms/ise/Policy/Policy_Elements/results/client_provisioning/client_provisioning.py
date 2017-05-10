from ui_poms.ise.Policy.Policy_Elements.results.results import Results
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
from selenium.webdriver.common.by import By



class  ClientProvisioning(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

##########    Page Actions And UI Elements     ###########

    @property
    def navigate_client_provisioning(self):
        return Button(By.XPATH, " (//*[contains(text(),'Client Provisioning')])[6]",self.driver)

    def navigate_from_parent(self):
        self.navigate_client_provisioning.click()

    def get_parent_page(self):
        return Results(self.app,  self.logger)



