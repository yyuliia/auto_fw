import pytest
from base.webdriver_factory import WebDriverFactory
from pages.home.login_page import Login


@pytest.yield_fixture(scope="class")
def one_time_set_up(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_browser_instance()

    if request.cls is not None:
        request.cls.driver = driver
        lp = Login(driver)
        lp.login('test@email.com', 'abcabc')

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")