from pages.courses.register_courses_page import CoursesPage
from utilities.test_status import AssertStatus
import unittest
import pytest


@pytest.mark.usefixtures("one_time_set_up")
class CoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.courses = CoursesPage(self.driver)
        self.as_status = AssertStatus(self.driver)

    def test_invalid_enrollment(self):
        self.courses.select_course_name('javascript')
        self.courses.select_course_to_enroll('JavaScript for beginners')
        self.courses.enroll_course('0000000000000000', '12/22', '123', '90120')
        result = self.courses.verify_enroll_failed()
        self.as_status.mark_final("test_invalid_enrollment", result, "enrollment failed")
