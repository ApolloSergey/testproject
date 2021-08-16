import logging
from selenium import webdriver
from project_constants import chromedriver_path
from project_constants import geckodriver_path
from selenium.webdriver.chrome.options import Options


class Browser(object):

    def set_browser(self, browser):
        driver = None
        logging.info("Browser: " + browser)
        if browser in "Chrome":
            chrome_options = Options()
            chrome_options.add_argument("--kiosk")
            driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
        elif browser in "Firefox":
            driver = webdriver.Firefox(executable_path=geckodriver_path)
            driver.fullscreen_window()
        return driver

    def get_browser(self, browser):
        return self.set_browser(browser)

    def open_webpage(self, driver, url):
        logging.info("Open web page: %s", str(url))
        driver.get(url)
        logging.debug("Web page has been opened")


browser_element = Browser()
