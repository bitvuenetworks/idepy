from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

class App:
    def __init__(self, selenium_url=None, browser='firefox', maximize=True):
        self.download_path = ''
        self.profile = None
        self.driver = None
        self.selenium_url = selenium_url
        self.browser = browser
        self.maximize = maximize
        self.profile = None
        self.is_remote = False

        if self.browser == 'firefox':
            self.capabilities = DesiredCapabilities.FIREFOX
            self.profile = webdriver.FirefoxProfile()
        elif self.browser == 'chrome':
            self.capabilities = DesiredCapabilities.CHROME
            # self.profile = Options()
        elif self.browser == 'internet explorer':
            self.capabilities = DesiredCapabilities.INTERNETEXPLORER
            self.profile = None
        else:
            raise Exception('Bad browser name')

        self.run()

    def run(self):
        """launching the web driver"""
        if self.selenium_url:
            self.driver = webdriver.Remote(command_executor=self.selenium_url,
                                           desired_capabilities=self.capabilities,
                                           browser_profile=self.profile)
        else:
            self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                           desired_capabilities=self.capabilities,
                                           browser_profile=self.profile)
        if self.maximize:
            self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def quit(self):
        """ when this object is killed, the running browser will be close"""
        self.driver.quit()

    def close(self):
        """ when this object is killed, the running browser will be close"""
        self.driver.close()


    @property
    def device(self):
        """ :return: the browser object"""
        return self.driver

    def timeout(self, time):
        self.driver.implicitly_wait(time)

    def switch_to_newwindow(self, number):
        self.number = number
        self.driver.switch_to_window(self.driver.window_handles[self.number])

    def switch_to_oldwindow(self):
        self.driver.switch_to_window(self.driver.window_handles[0])


if __name__ == '__main__':
    app = App()

