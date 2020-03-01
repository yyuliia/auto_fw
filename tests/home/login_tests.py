from selenium import webdriver
from pages.home.login_page import Login
import unittest
import pytest


@pytest.mark.usefixtures("one_time_set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.lp = Login(self.driver)

    def test_invalid_login(self):
        self.lp.login(password='abaabcabc')
        result = self.lp.verify_login_fail()
        assert result == True

    def test_valid_login(self):
        self.lp.login('test@email.com', 'abcabc')
        result = self.lp.verify_login_success()
        assert result == True
        result_title = self.lp.verify_title()
        assert result_title == True