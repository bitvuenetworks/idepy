from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By
from selenium_core.selenium_ui_elements import Button
from selenium_core.selenium_ui_elements import Link
from selenium_core.selenium_ui_elements import Input

from ui_poms.ise.Policy.Policy_Elements.Conditions.Authentication.Authentication import Authentication
import time

class SimpleConditions(BasePage):

        def __init__(self, app, logger):
            super(SimpleConditions, self).__init__(app, logger)

    # overriden methods------------------------------------------------------

        def navigate_from_parent(self):
            """Overrides from BasePage"""
            self.navigate_simple_conditions.click()

        def get_parent_page(self):
            """Overrides from BasePage"""
            return Authentication(self.app, self.logger)

    # navigation ui elements--------------------------------------------------

        @property
        def navigate_simple_conditions(self):
            return Link(By.XPATH,"//a[@href='#policy/policy_elements/policy_elements_conditions/authentication/authentication_simple']",self.driver)


        #page UI elements


        @property
        def simple_condition_add_button(self):
            return Button(By.ID,"authenSimpleConditionAddBtn",self.driver)



        #edit the button details
        @property
        def simple_condition_name(self):
            return Input(By.XPATH,".//*[@id='authenSimpleConditionName']",self.driver)
        @property
        def simple_condition_description(self):
            return Input(By.XPATH,".//*[@id='authenSimpleConditionDescription']",self.driver)




        def simple_condition_attribute(self):
            return Button(By.XPATH,".//*[@id='xwt_widget_form_IconDropDownButton_0']",self.driver)

        @property

        def simple_condition_attribute_edit_form(self):
            return Button(By.XPATH,".//*[@id='xwt_widget_objectselector__ObjectSelectorListItem_248']/div[2]",self.driver)

        def simple_condition_attribute_edit_forms_selection(self):
            return Button(By.XPATH,".//*[@id='xwt_widget_objectselector__ObjectSelectorListItem_305']/div[2]",self.driver)


        def add_simple_condition(self, name, description):
            self.wait_for_loader([self.simple_condition_add_button])
            self.simple_condition_add_button.click()
            time.sleep(5)
            self.fill_simple_condition_form(self, name, description)
            time.sleep(3)


        def fill_simple_condition_form(self, name, description, attribute):


            self.wait_for_loader([self.simple_condition_name])
            self.simple_condition_name.click()
            self.simple_condition_name.send_text(name)


            self.simple_condition_description.click()
            self.simple_condition_description.send_text(description)


