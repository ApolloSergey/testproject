from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.helpers.ui_helper import UiHelper


class AmazonPage(BasePage):
    """
    Locators and actions of the Amazon Page
    """

    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    GET_BOOK_PRICE = (By.ID, "price")
    NUMBER_OF_ITEM_IN_CART = (By.ID, "nav-cart-count")
    CHILDREN_BOOKS = (By.XPATH, "//span[contains(text(), \"Children's Books\")]")
    SHOPPING_CART = (By.XPATH, "//h1[contains(text(), 'Shopping Cart')]")
    GET_CART_TOTAL = (By.XPATH, "//span[@class='ewc-subtotal-amount']/span")
    CHECKOUT_CART = (By.XPATH, "//input[@name='proceedToRetailCheckout']")
    SIGN_IN_PAGE = (By.XPATH, "//h1[contains(text(), 'Sign-In')]")
    BOOK = "//div[@data-component-type='s-search-result']//span[contains(text(), '{}')]"
    BOOK_WITH_PRICE = "//span[contains(text(), '{}')]/ancestor::div[@data-name='Active Items']" \
                      "/descendant::span[contains(text(), '{}')]"
    A_GIFT = "//span[contains(text(), '{}')]/ancestor::div[@data-name='Active Items']" \
             "/descendant::input[@type='checkbox']"
    QUANTITY_VALUE_OPTION_SET = "//span[contains(text(), '{}')]/ancestor::div[@data-name='Active Items']" \
                                "/descendant::select[@name='quantity']"
    QUANTITY_VALUE = "//span[contains(text(), '{}')]/ancestor::div[@data-name='Active Items']" \
                     "/descendant::span[@class='a-dropdown-prompt']"
    GET_CART_SUBTOTAL = "//span[@id='sc-subtotal-amount-buybox']/span[contains(text(), '{}')]"

    def use_amazon_search(self, search_string):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.send_keys(search_string)
        search_box.send_keys(Keys.ENTER)

    def select_children_book_menu(self):
        self.use_amazon_search("Books")
        UiHelper.wait_till_element_clickable(self.driver, self.CHILDREN_BOOKS)
        self.driver.find_element(*self.CHILDREN_BOOKS).click()

    def perform_checkout(self):
        UiHelper.wait_till_element_clickable(self.driver, self.CHECKOUT_CART)
        self.driver.find_element(*self.CHECKOUT_CART).click()

    def find_and_select_book(self, book_name):
        self.use_amazon_search(book_name)
        book_locator = (By.XPATH, self.BOOK.format(book_name))
        UiHelper.wait_till_element_clickable(self.driver, book_locator)
        self.driver.find_element(*book_locator).click()

    def get_book_price(self):
        UiHelper.wait_till_element_clickable(self.driver, self.ADD_TO_CART)
        book_price = self.driver.find_element(*self.GET_BOOK_PRICE).text
        return book_price[1:]

    def get_cart_total(self):
        UiHelper.wait_till_element_clickable(self.driver, self.GET_CART_TOTAL)
        cart_total = self.driver.find_element(*self.GET_CART_TOTAL).text
        return cart_total[1:]

    def get_cart_item_count(self):
        item_count = self.driver.find_element(*self.NUMBER_OF_ITEM_IN_CART)
        return item_count.text

    def add_book_to_cart(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART)
        add_to_cart_button.click()

    def navigate_to_cart(self):
        UiHelper.wait_till_element_clickable(self.driver, self.NUMBER_OF_ITEM_IN_CART)
        self.driver.find_element(*self.NUMBER_OF_ITEM_IN_CART).click()

    def set_as_gift(self, book_name):
        UiHelper.wait_till_element_clickable(self.driver, self.NUMBER_OF_ITEM_IN_CART)
        checkbox_locator = (By.XPATH, self.A_GIFT.format(book_name))
        self.driver.find_element(*checkbox_locator).click()

    def set_quantity_value(self, book_name, quantity_value):
        quantity_locator = (By.XPATH, self.QUANTITY_VALUE_OPTION_SET.format(book_name))
        quantity = Select(self.driver.find_element(*quantity_locator))
        quantity.select_by_value(quantity_value)

    def get_quantity_value(self, book_name):
        quantity_locator = (By.XPATH, self.QUANTITY_VALUE.format(book_name))
        quantity = self.driver.find_element(*quantity_locator)
        return quantity.text

    def is_shopping_cart_displayed(self):
        return UiHelper.wait_till_element_clickable(self.driver, self.NUMBER_OF_ITEM_IN_CART)

    def is_book_with_price_displayed(self, book_name, book_price):
        book_with_price_locator = (By.XPATH, self.BOOK_WITH_PRICE.format(book_name, book_price))
        return UiHelper.wait_till_element_clickable(self.driver, book_with_price_locator)

    def is_gift_checkbox_selected(self, book_name):
        checkbox_locator = (By.XPATH, self.A_GIFT.format(book_name))
        book = self.driver.find_element(*checkbox_locator)
        return book.is_selected()

    def is_subtotal_displayed(self, subtotal_value):
        subtotal_value_locator = (By.XPATH, self.GET_CART_SUBTOTAL.format(subtotal_value))
        return UiHelper.wait_till_element_clickable(self.driver, subtotal_value_locator)

    def is_sign_in_page_displayed(self):
        return UiHelper.wait_till_element_clickable(self.driver, self.SIGN_IN_PAGE)

