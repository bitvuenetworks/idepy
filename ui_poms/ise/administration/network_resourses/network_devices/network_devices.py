from ui_poms.ise.administration.network_resourses.network_resourses import NetworkResourses
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Input
import time


class NetworkDevices(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,  logger)

    #page ui actions and elements


    @property
    def navigate_network_devices(self):
        return Button(By.XPATH,   "//a[@href='#administration/administration_networkresources/administration_networkresources_devices']",self.driver)

    def navigate_from_parent(self):
        self.navigate_network_devices.click()

    def get_parent_page(self):
        return NetworkResourses(self.app ,  self.logger)

#Page UI elements

    @property
    def network_device_add_button(self):
        return Button(By.XPATH, "//button[@id='NetDevAddBtn']",self.driver)

    @property
    def network_device_name(self):
        return Input(By.XPATH, "//input[@id='netDevDeviceName']", self.driver)

    @property
    def network_device_description(self):
        return Input(By.NAME, "networkDevice.description", self.driver)
    @property
    def network_device_IP_address(self):
        return Input(By.XPATH,  "(//input[@class='dijitReset'])[2]",self.driver)

    @property
    def network_device_modelname(self):
        return Input(By.ID, "netDevModelName", self.driver)

    @property
    def network_device_software_version(self):
        return Input(By.ID, "netDevSoftVer",  self.driver)

    @property
    def network_device_submit_button(self):
        return Button(By.ID,  "submitBtn",  self.driver)

    def add_nework_device(self,name,description,IP_address,modelname,software_version):
        self.wait_for_loader([self.network_device_add_button])
        self.network_device_add_button.click()
        time.sleep(3)

        self.fill_network_device_form(name,description,IP_address,modelname,software_version)
        time.sleep(8)

        self.network_device_submit_button.click()
        time.sleep(3)

    def fill_network_device_form(self,name,description,IP_address,modelname,software_version):
        self.wait_for_loader([self.network_device_name])
        self.network_device_name.click()
        self.network_device_name.send_text(name)
        time.sleep(3)

        self.network_device_description.click()
        self.network_device_description.send_text(description)
        time.sleep(3)

        self.network_device_IP_address.click()
        self.network_device_IP_address.send_text(IP_address)
        time.sleep(3)

        self.network_device_modelname.click()
        self.network_device_modelname.send_text(modelname)
        time.sleep(3)

        self.network_device_software_version.click()
        self.network_device_software_version.send_text(software_version)
        time.sleep(3)