from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import Link
from selenium_core.selenium_ui_elements import Input
from ui_poms.ise.workcenters.Guest_Access.Portals_Components import Portals_Components
import time

class Guest_Portals(BasePage):
    def __init__(self,app,logger):
        super(Guest_Portals,self).__init__(app,logger)



        #navigate UI elements and actions

    @property

    def navigate_guest_portals(self):
        return Link(By.XPATH, "//div[contains(text(),'Guest Portals')]", self.driver)


    def navigate_from_parent(self):
        self.navigate_guest_portals.click()


    def get_parent_page(self):
        return Portals_Components(self.app,self.logger)

    @property

    def guest_portals_Create_Button(self):
        return Button(By.XPATH,".//*[@id='guestAccessMainCreateBtn']",self.driver)

    #creation guest portal elements


    def Sponcerd_guest_portal_selection(self):
        return Button(By.XPATH,"//span[contains(text(),'Continue...')]",self.driver)

    def guest_portal_Name(self):
        return Input(By.ID,"portalName",self.driver)


    def guest_portal_Description(self):
        return Input(By.ID,"portalDescription",self.driver)


    def Save_Button(self):
        return Button(By.ID,"guestAccessSettingsCreateBtn",self.driver)



    def add_guest_portal(self,Name,Description):
        self.wait_for_loader([self.guest_portals_Create_Button])
        self.guest_portals_Create_Button.click()
        time.sleep(3)
        self.Sponcerd_guest_portal_selection().click()
        time.sleep(5)
        self.fill_guest_portal_form(Name,Description)
        time.sleep(10)
        self.Save_Button().click()

    def fill_guest_portal_form(self,Name,Description):
        self.guest_portal_Name().click()
        self.guest_portal_Name().send_text(Name)

        self.guest_portal_Description().click()
        self.guest_portal_Description().send_text(Description)