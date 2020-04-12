import utilities.custom_logger as cl
import logging
from base.base_page import BasePage


class NavigationPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = 'My Courses'
    _all_courses = 'All Courses'
    _practice = 'Practice'
    _user_icon = '//div//span[text()="Test"]'
    _home_link = '//a[contains(@class, "header-logo")]'

    def navigate_all_courses(self):
        self.element_click(self._all_courses, locator_type="link")

    def navigate_my_courses(self):
        self.element_click(self._my_courses, locator_type="link")

    def navigate_practice(self):
        self.element_click(self._practice, locator_type="link")

    def click_user_icon(self):
        user_icon_settings = self.wait_for_element(self._user_icon, locator_type="xpath", pollFrequency=1)
        self.element_click(element=user_icon_settings)

    def navigate_home_page(self):
        self.element_click(self._home_link, locator_type="xpath")
