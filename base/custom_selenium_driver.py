from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class CustomSeleniumDriver:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, result_message):
        """
        For screenshots
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_dir = "../screenshots/"
        relative_file = screenshot_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, relative_file)
        destination_dir = os.path.join(current_dir, screenshot_dir)

        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.log.info("Saved to " + destination_file)
        except:
            self.log.error("Exception!")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + "not supported")
        return False

    def switch_iframe(self, id="", name="", index=None):
        """
        Optional data
        :param id:
        :param name:
        :param index:
        :return: None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)


    def switch_default_content(self):
        self.driver.switch_to.default_content()

    def get_element_attribute(self, attribute, element=None, locator="", locator_type="id"):
        if locator:
            self.get_element(locator, locator_type)
        value = element.get_attribute(attribute)
        return value

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator + " and locator type: " + locator_type)
        except:
            self.log.info("Element not found")
        return element

    def get_element_list(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator + " and locator_type: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator + " and locator_type: " + locator_type)
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.log.info("Oooops! not clickable")
            print_stack()

    def send_data(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data to element with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.log.info("Oooops! can not send")
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) != 0:
                self.log.info("Getting text on element: " + info)
                self.log.info("The text is: " + text)
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            return False

    def is_element_enabled(self, locator, locator_type="id", info=""):
        element = self.get_element(locator, locator_type)
        enabled = False
        try:
            attribute_value = self.get_element_attribute(element, attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute(element, attribute="class")
                self.log.info("Attribute value from WEB: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :" + info + " is enabled")
            else:
                self.log.info("Element :" + info + " is not enabled")
        except:
            self.log.info("Element :" + info + " state could not be found")
        return enabled

    def elements_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " locator_type: " + locator_type)
            else:
                self.log.info("Element is not displayed with locator: " + locator + " locator_type: " + locator_type)
            return displayed
        except:
            print("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, pollFrequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to br clickable")
            wait = WebDriverWait(self.driver, 10, pollFrequency = 1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(by_type, locator))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def custom_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 800);")