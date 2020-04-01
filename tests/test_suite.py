import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_test_data_set import MultipleCoursesTest

# Get all tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(MultipleCoursesTest)

# Create a test suite combining all test casses
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)