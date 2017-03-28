from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import Link
from selenium_core.selenium_ui_elements import Input
from selenium_core.selenium_ui_elements import *
from ui_poms.ise.workcenters.Guest_Access.Portals_Components import Portals_Components
import time

class Guest_Portals(BasePage):
    def __init__(self,app,logger):
        super(Guest_Portals,self).__init__(app,logger)



        #navigate UI elements and actions

    @property

    def navigate_Guest_Portals(self):
        return Link(By.XPATH,".//*[@id='accordion']/li[1]/a/div",self.driver)


    def navigate_from_parent(self):
        self.navigate_Guest_Portals.click()


    def get_parent_page(self):
        return Portals_Components(self.app,self.logger)

    @property

    def Guest_Portals_Create_Button(self):
        return Button(By.XPATH,".//*[@id='guestAccessMainCreateBtn']",self.driver)

    #creation guest portal elements


    def Sponcerd_Guest_Portal_selection(self):
        return Button(By.XPATH,".//*[@id='xwt_widget_form_TextButton_46']",self.driver)

    def Guest_Portal_Name(self):
        return Input(By.ID,"portalName",self.driver)


    def Guest_Portal_Description(self):
        return Input(By.ID,"portalDescription",self.driver)


    def Save_Button(self):
        return Button(By.ID,"guestAccessSettingsCreateBtn",self.driver)



    def add_Guest_Portal(self,Name,Description):
        self.wait_for_loader(self.Guest_Portals_Create_Button)
        self.Guest_Portals_Create_Button.click()
        time.sleep(3)
        self.Sponcerd_Guest_Portal_selection().click()
        time.sleep(5)
        self.fill_Guest_Portal_form(Name,Description)
        time.sleep(10)
        self.Save_Button().click()

    def fill_Guest_Portal_form(self,Name,Description):
        self.Guest_Portal_Name().click()
        self.Guest_Portal_Name().send_text(Name)

        self.Guest_Portal_Description().click()
        self.Guest_Portal_Description().send_text(Description)
