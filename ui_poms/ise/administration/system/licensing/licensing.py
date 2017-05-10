from selenium_core.selenium_ui_elements import *
from selenium_core.selenium_ui_base_page import BasePage
from ui_poms.ise.administration.system.system import System

class Licensing(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

#Navigating UI Elements and Actions


    @property

    def navigate_licensing(self):
         return Link(By.XPATH, "//a[contains(@href,'#administration/administration_system/administration_system_licensing')]", self.driver)

    def navigate_from_parent(self):
        self.navigate_licensing.click()

    def get_parent_page(self):
        return System(self.app, self.logger)


#Page UI Elements


    @property
    def cisco_smart_licensing(self):
        return Link(By.XPATH, "(//span[contains(text(),'Cisco Smart Licensing')])[1]", self.driver)


    @property
    def connecton_method(self):
        return Button(By.XPATH, ".//*[@id='widget_transportMode']/div/div[1]/div[1]", self.driver)

    @property
    def connection_method_drop_down(self):
        return Button(By.XPATH, "//li[@id='transportMode_popup0']",self.driver)

    @property
    def enable_button(self):
        return Button(By.ID, "slSubmitId",self.driver)

    @property
    def enable_popup(self):
        return Button(By.XPATH, "(//span[contains(text(), 'Yes')]) [last()]",self.driver)


    #page actions

    def add_licensing_page(self):
      self.wait_for_loader([self.cisco_smart_licensing])
      self.cisco_smart_licensing.click()
      time.sleep(3)

      self.connecton_method.click()
      time.sleep(3)

      self.connection_method_drop_down.click()
      time.sleep(3)

      self.enable_button.click()
      time.sleep(5)

      self.enable_popup.click()
      time.sleep(3)

      #self.fill_licensing_page_form(connection_method)
      #time.sleep(8)

    #def fill_licensing_page_form(self):
     #   self.wait_for_loader([self.connecton_method])
       # time.sleep(5)
      #  self.connecton_method.click()
       # self.connecton_method.send_text(connection_method)


