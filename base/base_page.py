from base.custom_selenium_driver import CustomSeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(CustomSeleniumDriver):

    def __init__(self, driver):
        """
        Init for base class

        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, title_to_verify):
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False