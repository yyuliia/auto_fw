import utilities.custom_logger as cl
import logging
from traceback import print_stack
from base.base_page import Base_Page


class TestStatus(Base_Page):

    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.resultList.append("Pass")
                    self.log.info("Verification successful :: + " + result_message)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("Verification failed :: + " + result_message)
                    self.take_screenshot(result_message)
            else:
                self.resultList.append("FAIL")
                self.log.error("Verification failed :: + " + result_message)
                self.take_screenshot(result_message)
        except:
            self.resultList.append("FAIL")
            self.log.error("Exception!")
            self.take_screenshot(result_message)
            print_stack()

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        self.set_result(result, result_message)

        if "FAIL" in self.resultList:
            self.log.error(test_name + " something went wrong")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(test_name + " test successful")
            self.resultList.clear()
            assert True == True