import pytest
from utils.browser import Browser


@pytest.fixture()
def base_driver_setup_amazon(request):
    browser = Browser()
    driver = browser.get_browser("Chrome")
    browser.open_webpage(driver, "https://www.amazon.com/")
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def base_driver_setup_the_internet(request):
    browser = Browser()
    driver = browser.get_browser("Firefox")
    browser.open_webpage(driver, "http://the-internet.herokuapp.com/")
    request.cls.driver = driver
    yield
    driver.quit()

