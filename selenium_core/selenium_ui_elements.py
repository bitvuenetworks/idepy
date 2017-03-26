import logging
import time
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

log = logging.getLogger()


class BaseElement(object):
    def __init__(self, by, id, driver, logger=log):
        self.by = by
        self.id = id
        self.driver = driver

    @property
    def element(self):
        return self.driver.find_element(self.by, self.id)


    """
     this function will check if the element is exist on current page
     the parmenters are how = which why to sreach the element (e.g. 'By.XPATH') and what will be the element itself (e.g."//*[text()[contains(.,'test')]]")
    """
    def is_element_present(self, how, what):
        log.info("Waiting for element " + what)
        try:

            self.driver.find_element(by=how, value=what)
            log.info("Found element " + what)
        except NoSuchElementException as e:
            log.info("Could not find element: " + what)
            return False
        return True

    def is_element_displayed(self):
        log.info("Waiting for element ")
        try:
            displaystatus = self.driver.find_element(self.by, self.id).is_displayed()
            if displaystatus:
                log.info("Found element ")
                return True
            else:
                return False
        except:
            log.info("Could not find element: ")
            return False


    def scroll_down_in_broswer(self):

        # using the JavaScriptExecutor to scroll down to bottom of window
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up_in_broswer(self):

        # using the JavaScriptExecutor to scroll down to bottom of window
        self.driver.execute_script("window.scrollTo(0,0)")

    def wait_for_element(self, timeout=30):
        log.info("Waiting for element " + self.id)
        current_time = time.time()
        while timeout > time.time() - current_time:
            try:
                self.driver.find_element(self.by, self.id)
                log.info("Found element: " + self.id)
                return True
            except:  # keep looping until timeout
                pass
        log.info("Could not find element: " + self.id)
        return False

    def screenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file('screenshot-{}.png'.format(now))

    def click(self, do_move=True):
        try:
            if do_move:
                log.info("Moving to element: " + self.id)
                ActionChains(self.driver).move_to_element(self.driver.find_element(self.by, self.id)).perform()
            log.info("Clicking element: " + self.id)
            self.driver.find_element(self.by, self.id).click()
        except Exception as e:
            print(e)
            self.screenshot()

    def hover(self):
        log.info("Hovering on element: " + self.id)
        ActionChains(self.driver).move_to_element(self.element).perform()

    def focus(self):
        log.info("Focusing on element: " + self.id)
        self.driver.execute_script(self.get_element_js_str() + ".focus()")

    def blur(self):
        log.info("Blurring element: " + self.id)
        self.driver.execute_script(self.get_element_js_str() + ".blur()")

    def get_element_js_str(self):
        if self.by is By.ID:
            return "document.getElementById(\"" + self.id + "\")"
        elif self.by is By.NAME:
            return "document.getElementsByName(\"" + self.id + "\")[0]"
        elif self.by is By.XPATH:
            return "document.evaluate(\"" + self.id + "\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;"

    def get_text(self):
        element = self.driver.find_element(self.by, self.id)
        return element.text

    def is_enabled(self):
        """Method to check whether element is enabled or not
         Return True if element is enabled else return False"""
        element = self.driver.find_element(self.by, self.id)
        return element.is_enabled()

    def presskey(self, key):
        """ Exmple usage of method presskey(Keys.TAB)"""
        """Method to press any key
           Need to add further code for other keys based on requirements"""
        action = ActionChains(self.driver)
        action.send_keys(key)
        action.perform()

    def scroll_to_element(self):
        """Method is used to scroll the page horizontally to specified element"""
        self.driver.execute_script("return arguments[0].scrollIntoView();", self.driver.find_element(self.by, self.id))
        return self

    def scroll_to_top_of_page(self):
        """ Method is used to scroll the page horizontally to top of page"""
        self.driver.execute_script("window.scrollTo(0, 0)")

    def get_attribute_value(self, attribute_name):
        return self.element.get_attribute(attribute_name)

    def get_class(self):
        return self.driver.find_element(self.by, self.id).get_attribute("class")


class Label(BaseElement):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)


class Input(BaseElement):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

    def send_text(self, text, clear=True):
        log.info("Sending text '" + text + "' to element: " + self.id)
        if clear:
            self.driver.find_element(self.by, self.id).clear()
        self.driver.find_element(self.by, self.id).send_keys(text)

    def send_enter(self):
        log.info("Sending Enter key" + self.id)
        self.driver.find_element(self.by, self.id).send_keys(Keys.ENTER)


class Button(BaseElement):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)


class Link(BaseElement):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)


class Hover(BaseElement):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

    def hover(self):
        log.info("Hovering on element: " + self.id)
        ActionChains(self.driver).move_to_element(self.element).perform()


class CheckBox(BaseElement):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

    def select(self):
        log.info("Selecting element: " + self.id)
        if not self.driver.find_element(self.by, self.id).is_selected():
            self.click()

    def deselect(self):
        log.info("Deselecting element: " + self.id)
        if self.driver.find_element(self.by, self.id).is_selected():
            self.click()

    def select_based_on_var(self, var):
        """Selects/Deselects this checkbox based on the value of var
        :param var: if True, select the checkbox, else deselect it
        """
        if var:
            self.select()
        else:
            self.deselect()


class SelectDropDown(BaseElement):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

    def select_option(self, option):
        """ Selects the specified option
        :param option: the text of the option as it appears on UI
        """
        log.info("Selecting option '" + option + "' on element: " + self.id)
        select = Select(self.driver.find_element(self.by, self.id))
        select.select_by_visible_text(option)

    def select_option_by_value(self, indexvalue):
        log.info("Selecting option at index:'" + str(indexvalue) + "' on element: " + self.id)
        select = Select(self.driver.find_element(self.by, self.id))
        select.select_by_index(indexvalue)


class RadioButton(BaseElement):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

class Div(BaseElement,):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

class Td(BaseElement,):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

class Span(BaseElement,):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

class Form(BaseElement,):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)

class Table(BaseElement,):
    def __init__(self, by, id, driver):
        super().__init__(by, id, driver)
