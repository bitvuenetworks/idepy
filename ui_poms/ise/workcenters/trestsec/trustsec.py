from ui_poms.ise.workcenters.workcenters import WorkCenters
from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import *


class TrustSec(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

# UI Elementgs and Page Actiions

    @property
    def navigate_trustsec(self):
        return Hover(By.XPATH,"//a[contains(@href,'workcenters/workcenter_trustsec')]",  self.driver)

    def navigate_from_parent(self):
        self.navigate_trustsec.hover()

    def get_parent_page(self):
        return WorkCenters(self.app,  self.logger)