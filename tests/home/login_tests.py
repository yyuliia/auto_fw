from selenium import webdriver
from utilities.test_status import TestStatus
from pages.home.login_page import Login
import unittest
import pytest


@pytest.mark.usefixtures("one_time_set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.lp = Login(self.driver)
        self.ts = TestStatus(self.driver)

    def test_invalid_login(self):
        self.lp.login(password='abaabcabc')
        result = self.lp.verify_login_fail()
        self.ts.mark(result, "good to go")

    def test_valid_login(self):
        result_title = self.lp.verify_title()
        self.ts.mark(result_title, "should fail")
        self.lp.login('test@email.com', 'abcabc')
        result = self.lp.verify_login_success()
        self.ts.mark_final("test_valid_login", result, "should be valid")
