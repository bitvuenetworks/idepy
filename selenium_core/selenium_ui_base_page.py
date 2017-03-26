import time
import logging
log = logging.getLogger()


class BasePage(object):

    def __init__(self, app, logger=log):
        self.driver = app.device
        self.app = app
        self.logger = logger


    # navigation UI elements and actions -------------------------------------------------------------------------------

    def navigate_to_page(self):
        """ Call this publicly to navigate to the implementing page
        This method should not be overriden
        """
        parent = self.get_parent_page()
        if parent:
            parent.navigate_to_page()
            time.sleep(3)
        self.navigate_from_parent()

    def navigate_from_parent(self):
        """ Navigates to the current page. This is used only in navigate_to_page()
        When this is called from navigate_to_page() it's guaranteed that the parent is already loaded
        """
        raise NotImplementedError()

    def get_parent_page(self):
        """ Get the parent page. This is used only in navigate_to_page()
        eg. return BasePage(self.app)
        """
        raise NotImplementedError()

    def wait_for_loader(self, element_list, timeout=60):
        """ the function check that all element given in the list was loaded to the page in the given timeout
        :param element_list: element to check the was loaded
        :param timeout: default is 30 sec
        :raise: Exception when not all page element were found
        """
        current_time = time.time()
        # self.logger.info("Waiting for elements to load on page")
        while len(element_list) > 0 and timeout > time.time() - current_time:
            for e in element_list:
                if e.wait_for_element():
                    element_list.remove(e)  # remove from waiting list when element found.
                    # self.logger.info("UI element {element.id} has loaded".format(element=e))

        if len(element_list) > 0:
            raise Exception("not all page element were loaded in timeout:{}".format(timeout))
