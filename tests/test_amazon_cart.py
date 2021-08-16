import pytest
from pages.amazon_page import AmazonPage
from utils.helpers.verify import Verify


class TestAmazonCart:
    """
    Add items to Amazon cart
    """

    bronco_book = "Bronco and Friends: A Party to Remember"
    baby_university_book = "Baby University Complete \"for Babies\" Board Book Set"
    quantity_value = '5'

    @pytest.mark.usefixtures("base_driver_setup_amazon")
    def test_amazon_cart(self):

        amazon_page = AmazonPage(self.driver)
        amazon_page.select_children_book_menu()
        amazon_page.find_and_select_book(self.bronco_book)
        bronco_book_price = amazon_page.get_book_price()
        amazon_page.add_book_to_cart()

        Verify.equals(amazon_page.get_cart_item_count(), '1', "Item isn't added to cart")
        Verify.equals(bronco_book_price, amazon_page.get_cart_total(), "Item isn't added to cart")

        amazon_page.find_and_select_book(self.baby_university_book)
        baby_university_book_price = amazon_page.get_book_price()
        amazon_page.add_book_to_cart()

        Verify.equals(amazon_page.get_cart_item_count(), '2', "Item isn't added to cart")
        Verify.equals(str(float(bronco_book_price) + float(baby_university_book_price)),
                      amazon_page.get_cart_total(), "Incorrect books total")

        amazon_page.navigate_to_cart()

        Verify.true(amazon_page.is_shopping_cart_displayed(), "Shopping cart page is missing")
        Verify.true(amazon_page.is_book_with_price_displayed(self.bronco_book, bronco_book_price),
                    "Book and price are missing")
        Verify.true(amazon_page.is_book_with_price_displayed(self.baby_university_book, baby_university_book_price),
                    "Book and price are missing")

        amazon_page.set_as_gift(self.bronco_book)

        Verify.true(amazon_page.is_gift_checkbox_selected(self.bronco_book), "Book isn't set as a gift")

        amazon_page.set_quantity_value(self.baby_university_book, self.quantity_value)

        Verify.equals(amazon_page.get_quantity_value(self.baby_university_book),
                      self.quantity_value, "Wrong quantity value ")

        subtotal = str(float(bronco_book_price) + (float(baby_university_book_price)*float(self.quantity_value)))

        Verify.true(amazon_page.is_subtotal_displayed(subtotal), "Wrong subtotal is displayed")

        amazon_page.perform_checkout()

        Verify.true(amazon_page.is_sign_in_page_displayed(), "Sign in page isn't displayed")





