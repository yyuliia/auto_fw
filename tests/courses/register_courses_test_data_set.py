from pages.courses.register_courses_page import CoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.test_status import AssertStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_csv_data import get_csv_data


@pytest.mark.usefixtures("one_time_set_up")
@ddt
class MultipleCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_set_up):
        self.courses = CoursesPage(self.driver)
        self.as_status = AssertStatus(self.driver)
        self.navigation = NavigationPage(self.driver)

    def setUp(self):
        self.courses.custom_scroll(direction="up")
        self.navigation.navigate_home_page()
        self.navigation.navigate_all_courses()

    @data(*get_csv_data("testdata.csv"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv, cc_postal):

        self.courses.select_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvv, cc_postal)
        result = self.courses.verify_enroll_failed()
        self.as_status.mark_final("test_invalid_enrollment", result, "enrollment failed")

