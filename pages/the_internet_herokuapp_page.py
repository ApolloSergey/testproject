from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.helpers.ui_helper import UiHelper


class TheInternetHeroPage(BasePage):
    """
    Locators and actions of the The Internet Hero Page
    """

    DROP_DOWN = (By.ID, "dropdown")
    LIST_ITEM = "//ul//a[contains(text(), '{}')]"
    PAGE_NAME = "//h3[contains(text(), '{}')]"
    BUTTONS = (By.XPATH, "//div[@class='large-2 columns']/a[contains(@class, 'button')]")
    BUTTON = "//a[contains(@class, 'button') and contains(text(), '{}')]"
    TABLE_ITEM = "//td[contains(text(), '{}')]"
    TABLE_ACTION = "//tr[{}]//td/a[contains(text(), '{}')]"

    def select_list_item(self, item_name):
        item_locator = (By.XPATH, self.LIST_ITEM.format(item_name))
        UiHelper.wait_till_element_clickable(self.driver, item_locator)
        self.driver.find_element(*item_locator).click()

    def set_dropdown_value(self, value):
        UiHelper.wait_till_element_clickable(self.driver, self.DROP_DOWN)
        quantity = Select(self.driver.find_element(*self.DROP_DOWN))
        quantity.select_by_visible_text(value)

    def get_selected_value(self):
        selected_option = Select(self.driver.find_element(*self.DROP_DOWN))
        return selected_option.first_selected_option.text

    def is_page_displayed(self, page_name):
        page_locator = (By.XPATH, self.PAGE_NAME.format(page_name))
        return UiHelper.wait_till_element_clickable(self.driver, page_locator)

    def get_button_names(self):
        list_buttons = []
        items = self.driver.find_elements(*self.BUTTONS)
        for i in items:
            list_buttons.append(i.text)
        return list_buttons

    def select_button_by_name(self, button_name):
        button_locator = (By.XPATH, self.BUTTON.format(button_name))
        UiHelper.wait_till_element_clickable(self.driver, button_locator)
        self.driver.find_element(*button_locator).click()

    def find_item_in_table(self, item_name):
        button_locator = (By.XPATH, self.TABLE_ITEM.format(item_name))
        return self.driver.find_element(*button_locator)

    def find_table_action(self, table_row, action_name):
        action_locator = (By.XPATH, self.TABLE_ACTION.format(table_row, action_name))
        return self.driver.find_element(*action_locator)

