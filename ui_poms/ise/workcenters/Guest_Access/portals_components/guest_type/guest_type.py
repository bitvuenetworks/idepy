from ui_poms.ise.workcenters.Guest_Access.portals_components.Portals_Components import PortalsComponents
from selenium_core.selenium_ui_base_page import BasePage
from selenium_core.selenium_ui_elements import Input
from selenium_core.selenium_ui_elements import Link
from selenium_core.selenium_ui_elements import Button
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import *
import time

class GuestType(BasePage):
    def __init__(self,app,logger):
        super().__init__(app,logger)

    #   Page UI Elements And Actions

    @property

    def navigate_guest_type(self):
        return Button(By.XPATH,  "//div[contains(text(),'Guest Types')]", self.driver)

    def navigate_from_parent(self):
        self.navigate_guest_type.click()

    def get_parent_page(self):
        return PortalsComponents(self.app,  self.logger)

### Page Elements

    @property
    def guest_type_create_button(self):
        return Button(By.ID,  "guestAccessGuestTypeCreateBtn",  self.driver)

    @property
    def guest_type_name(self):
        return Input(By.ID, "guestTypeStub.name",   self.driver)


    @property
    def guest_type_description(self):
        return Input(By.ID,  "guestTypeStub.description",   self.driver)

    @property
    def guest_type_duration_day(self):
        return Input(By.ID,  "guestTypeStub.maxTime",  self.driver)

    @property
    def guest_type_specific_time_button(self):
        return Button(By.ID,  "restrictFlag",    self.driver)

    @property
    def guest_type_specific_time_dropdown(self):
        return Button(By.CLASS_NAME,   "dijitReset",   self.driver)

    @property
    def guest_type_specific_time_dropdown_selection(self):
        return Button(By.CLASS_NAME,  "dijitTimePickerItemInner",   self.driver)

    @property
    def guest_type_closing_time_dropdown(self):
        return Button(By.CLASS_NAME,  "dijitReset",   self.driver)

    @property
    def guest_type_closing_time_dropdown_selection(self):
        return Button(By.CLASS_NAME,  "dijitTimePickerItemInner",   self.driver)

    @property
    def guest_type_expiry_notification(self):
        return Button(By.ID,  "guestTypeStub.notifyFlag",   self.driver)

    @property
    def  guest_type_save_button(self):
        return Button(By.ID,  "guestTypeSaveBtn", self.driver)

    def add_guest_type(self,name,description,duration_day,):
        self.wait_for_loader([self.guest_type_create_button])
        self.guest_type_create_button.click()
        time.sleep(5)

        self.fill_guest_type_form(name,description,duration_day)
        time.sleep(15)

        self.guest_type_specific_time_button.click()
        time.sleep(2)

        self.guest_type_specific_time_dropdown.click()
        time.sleep(2)

        self.guest_type_specific_time_dropdown_selection.click()
        time.sleep(2)

        self.guest_type_closing_time_dropdown.click()
        time.sleep(2)

        self.guest_type_closing_time_dropdown_selection.click()
        time.sleep(5)

        self.guest_type_expiry_notification.scroll_down_in_broswer()
        self.guest_type_expiry_notification.click()
        time.sleep(5)


        self.guest_type_save_button.scroll_to_top_of_page()
        self.guest_type_save_button.click()
        time.sleep(3)


    def fill_guest_type_form(self,name,description,duration_day):
        self.wait_for_loader([self.guest_type_name])
        self.guest_type_name.click()
        self.guest_type_name.send_text(name)
        time.sleep(3)

        self.guest_type_description.click()
        self.guest_type_description.send_text(description)
        time.sleep(3)

        self.guest_type_duration_day.click()
        self.guest_type_duration_day.send_text(duration_day, clear=True)
        time.sleep(3)
