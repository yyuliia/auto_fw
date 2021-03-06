import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.base_page import BasePage


class Login(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navigation = NavigationPage(driver)

    # Locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'
    _logout_link = 'Log Out'

    def click_login_link(self):
        self.element_click(self._login_link, locator_type="link")

    def enter_email(self, email):
        self.send_data(email, self._email_field)

    def enter_password(self, password):
        self.send_data(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="name")

    def login(self, email="", password=""):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_success(self):
        result = self.is_element_present("//div//span[text()='Test']", locator_type="xpath")
        return result

    def verify_login_fail(self):
        result = self.is_element_present("//div[contains(text(),'Invalid email or password.')]", locator_type="xpath")
        return result

    def verify_title(self):
       return self.verify_page_title("Let's Kode It")

    def logout(self):
        self.navigation.click_user_icon()
        logout_link_element = self.wait_for_element(self._logout_link, locator_type="link", pollFrequency=1)
        self.element_click(element=logout_link_element)
