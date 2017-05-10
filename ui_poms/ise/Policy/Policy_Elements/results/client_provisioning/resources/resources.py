from ui_poms.ise.Policy.Policy_Elements.results.client_provisioning.client_provisioning import ClientProvisioning
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import *


class Resources(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

##   Page ui elements and Page actions          ###############

    @property
    def navigate_resources(self):
        return Button(By.XPATH,  "(//*[contains(text(),'Resources')])[4]", self.driver)

    def navigate_from_parent(self):
        self.navigate_resources.click()

    def get_parent_page(self):
        return ClientProvisioning(self.app,   self.logger)


    #########   UI Elements   ##############3

    @property
    def resources_add_button(self):
        return Button(By.ID, "resourceListAddBtn",  self.driver)

    @property
    def resources_navtive_supplicant_selection(self):
        return Button(By.XPATH, "(//*[contains(text(),'Native Supplicant Profile')])[6]",self.driver)



    @property
    def resourses_profile_name(self):
        return Input(By.ID, "configName",self.driver)

    @property
    def resources_profile_description(self):
        return Input(By.ID,  "configDesc",self.driver)

    @property
    def resources_selecting_operating_system_dropdown(self):
        return Button(By.XPATH,  ".//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand']" ,  self.driver)

    @property
    def resources_selecting_operating_system_inner_dropdown(self):
        return Button(By.XPATH, ".//*[@class='dijitReset dijitInline xwt-IconDropDownButtonNode']",  self.driver)

    @property
    def resources_selecting_os_itemnode(self):
        return Button(By.XPATH, ".//*[@id='osItemNavNode']",self.driver)

    @property
    def resources_selecting_windows_all(self):
        return Button(By.XPATH,  "(.//*[@id='osItemNavNode'])[5]",self.driver)

    @property
    def resources_selecting_windows_version(self):
        return  Button(By.XPATH,".//*[contains(text(),'Windows 7 (All)')]",self.driver)

    @property
    def resources_wirless_profile_add_button(self):
        return Button(By.XPATH,".//*[@id='spwCSAddBtn']",self.driver)

    @property
    def resources_wireless_profile_SSIDname(self):
        return Input(By.ID, "ssid",self.driver)

    @property
    def resources_wireless_profile_autoconfig_url(self):
        return Input(By.ID,  "WirelessProxyAddress",self.driver)

    @property
    def resources_wireless_profile_proxy_hostip(self):
        return Input(By.ID, "proxyHost",self.driver)

    @property
    def resources_wireless_profile_proxy_port(self):
        return Input(By.XPATH, "(.//*[@class='dijitReset'])[5]",self.driver)

    @property
    def resources_wireless_profile_security_dropdown(self):
        return Button(By.XPATH,  "(.//*[@class='dijitReset dijitArrowButtonInner'])[6]",self.driver)

    @property
    def resources_wireless_profile_security_selection(self):
        return Button(By.XPATH,  "(//td[@class='dijitReset dijitMenuItemLabel'])[3]",self.driver)

    @property
    def resources_wireless_profile_protocol(self):
        return Button(By.XPATH,  "(.//*[@class='dijitReset dijitArrowButtonInner'])[7]", self.driver)

    @property
    def resources_wireless_profile_protocol_selection(self):
        return  Button(By.XPATH,  ".//*[contains(text(),'TLS')]",self.driver)

    @property
    def resources_wireless_profile_save_button(self):
        return Button(By.ID,  "csSaveBtn",self.driver)
    @property
    def resources_submit_button(self):
        return Button(By.ID, "spwSaveBtn", self.driver)



    def add_resources_profile(self,name,description,SSIDname,auto_config_url,proxy_hostip,proxy_port):
        self.wait_for_loader([self.resources_add_button])

        self.resources_add_button.click()
        time.sleep(3)

        self.resources_navtive_supplicant_selection.click()
        time.sleep(3)

        self.fill_resources_profile_form(name,description,SSIDname,auto_config_url,proxy_hostip,proxy_port)
        time.sleep(8)


        self.resources_submit_button.click()
        time.sleep(3)

    def fill_resources_profile_form(self,name,description,SSIDname,auto_config_url,proxy_hostip,proxy_port):
        self.wait_for_loader([self.resourses_profile_name])

        self.resourses_profile_name.click()
        self.resourses_profile_name.send_text(name)
        time.sleep(2)

        self.resources_profile_description.click()
        self.resources_profile_description.send_text(description)
        time.sleep(2)

        self.resources_selecting_operating_system_dropdown.click()
        time.sleep(3)

        self.resources_selecting_operating_system_inner_dropdown.click()
        time.sleep(3)

        self.resources_selecting_os_itemnode.click()
        time.sleep(3)

        self.resources_selecting_windows_all.click()
        time.sleep(3)

        self.resources_selecting_windows_version.click()
        time.sleep(3)


        self.resources_wirless_profile_add_button.click()
        time.sleep(3)

        self.resources_wireless_profile_SSIDname.click()
        self.resources_wireless_profile_SSIDname.send_text(SSIDname)

        self.resources_wireless_profile_autoconfig_url.click()
        self.resources_wireless_profile_autoconfig_url.send_text(auto_config_url)
        time.sleep(2)

        self.resources_wireless_profile_proxy_hostip.click()
        self.resources_wireless_profile_proxy_hostip.send_text(proxy_hostip)
        time.sleep(2)

        self.resources_wireless_profile_proxy_port.click()
        self.resources_wireless_profile_proxy_port.send_text(proxy_port)
        time.sleep(2)


        self.resources_wireless_profile_security_dropdown.click()
        time.sleep(3)

        self.resources_wireless_profile_security_selection.click()
        time.sleep(3)

        self.resources_wireless_profile_protocol.click()
        time.sleep(3)

        self.resources_wireless_profile_protocol_selection.click()
        time.sleep(3)

        self.resources_wireless_profile_save_button.click()
        time.sleep(3)
