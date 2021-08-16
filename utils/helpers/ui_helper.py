from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class UiHelper(object):
    """
    All actions from selenium that are common.
    """

    @staticmethod
    def wait_till_element_clickable(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, TimeoutException))
        try:
            UiHelper.wait_till_element_is_displayed(driver, locator, timeout=int(timeout))
            wait.until(ec.element_to_be_clickable(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def wait_till_element_is_displayed(driver, locator, timeout=5):
        """
        :return: True if element IS displayed
        """
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
