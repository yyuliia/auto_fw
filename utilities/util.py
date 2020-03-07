import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging


class Util:

    log = cl.custom_logger(logging.INFO)

    def sleep(self, sec, info=""):
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "'seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def get_alpha_numeric(self, length, alpha_type='letters'):
        alpha_num = ''
        if alpha_type == 'lower':
            case = string.ascii_lowercase
        elif alpha_type == 'upper':
            case = string.ascii_uppercase
        elif alpha_type == 'digits':
            case = string.digits
        elif alpha_type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for symbol in range(length))

    def get_unique_name(self, char_count=10):
        return self.get_alpha_numeric(char_count, 'lower')

    def get_unique_namelist(self, list_size=5, item_length=None):
        name_list = []
        for name in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[name]))
        return name_list

    def verify_text_contains(self, actual_text, expected_text):
        self.log.info("Actual text from Application -> :: " + actual_text)
        self.log.info("Expected text from Application -> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("Contains")
            return True
        else:
            self.log.info("Does not contains")
            return False

    def verify_text_match(self, actual_text, expected_text):
        self.log.info("Actual text from Application -> :: " + actual_text)
        self.log.info("Expected text from Application -> :: " + expected_text)
        if expected_text.lower() == actual_text.lower():
            self.log.info("Matched")
            return True
        else:
            self.log.info("Does not matched")
            return False

    def verify_lists_match(self, actual_list, expected_list):
        return set(expected_list) == set(actual_list)

    def verify_lists_contains(self, actual_list, expected_list):
        length = len(expected_list)
        for list_element in range(0, length):
            if expected_list[list_element] not in actual_list:
                return False
        else:
            return False