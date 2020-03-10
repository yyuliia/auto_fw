import utilities.custom_logger as cl
import logging
from base.base_page import BasePage


class CoursesPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# find out _locators

    _search_box = 'search-courses' # by id
    _search_box_button = 'search-course-button' # by id
    _course = '//div[contains(@class, "course-listing-title") and contains(text(), "{0}")]' # by xpath
    _enroll_button = 'enroll-button-top' # by id
    _credit_card_input = '//input[@aria-label="Credit or debit card number"]' # by xpath
    _credit_card_exp = 'exp-date' # by name
    _credit_card_cvv = '//input[@name="cvc"]' #by xpath
    _postal_code = 'postal' # by name
    _agreed_to_terms = '//input[@id="agreed_to_terms_checkbox"]' # by xpath
    _submit_enroll = 'confirm-purchase' # by id

    def select_course_name(self, name):
        self.send_data(name, self._search_box)
        self.element_click(self._search_box_button)

    def select_course_to_enroll(self, full_course_name):
        self.element_click(self._course.format(full_course_name), locator_type='xpath')

    def click_enroll_button(self):
        self.element_click(self._enroll_button)

    def enter_card_num(self, num):
        self.switch_iframe(name="__privateStripeFrame8")
        self.send_data(num, self._credit_card_input, locator_type='xpath')
        self.switch_default_content()

    def enter_card_exp(self, exp):
        self.switch_iframe(name="__privateStripeFrame9")
        self.send_data(exp, self._credit_card_exp, locator_type='name')
        self.switch_default_content()

    def enter_card_cvv(self, cvv):
        self.switch_iframe(name="__privateStripeFrame10")
        self.send_data(cvv, self._credit_card_cvv, locator_type='xpath')
        self.switch_default_content()

    def enter_postal_code(self, post_code):
        self.switch_iframe(name="__privateStripeFrame11")
        self.send_data(post_code, self._postal_code, locator_type='name')
        self.switch_default_content()

    def agree_terms(self):
        self.element_click(self._agreed_to_terms, locator_type='xpath')

    def click_submit_button(self):
        self.element_click(self._submit_enroll)

    def enter_credit_card_info(self, num, exp, cvv, post_code):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)
        self.enter_postal_code(post_code)

    def enroll_course(self, num="", exp="", cvv="", post_code=""):
        self.click_enroll_button()
        self.custom_scroll(direction="down")
        self.enter_credit_card_info(num, exp, cvv, post_code)
        self.agree_terms()
        self.click_submit_button()
    """
    1. click on the enroll button
    2. scroll down
    3. eneter creadit card info
    4. click enroll in course button
    :param self: 
    :param num: 
    :param exp: 
    :param cvv: 
    :return: 
    """

    def verify_enroll_failed(self):
        result = self.is_element_enabled(self._submit_enroll, info="Enroll Button")
        return not result

