from ui_poms.ise.workcenters.trestsec.trustsec import TrustSec
from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import *

class Components(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    ###  Page UI Elements and Actions


    @property
    def navigate_components(self):
        return Button(By.XPATH, "//a[@href='#workcenters/workcenter_trustsec/workcenter_trustsec_components']", self.driver )

    def  navigate_from_parent(self):
        self.navigate_components.click()

    def get_parent_page(self):
        return TrustSec(self.app,  self.logger)