from base.custom_selenium_driver import CustomSeleniumDriver
import utilities.custom_logger as cl
import logging


class Login(CustomSeleniumDriver):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

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
        if "Let's Kode It" in self.get_title():
            return True
        else:
            return False