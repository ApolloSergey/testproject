import pytest
from pages.the_internet_herokuapp_page import TheInternetHeroPage
from utils.helpers.verify import Verify


class TestTheInternetHero:
    """
    Tests from http://the-internet.herokuapp.com/
    """

    @pytest.mark.usefixtures("base_driver_setup_the_internet")
    def test_select_drop_down(self):
        option_set_value = "Option 2"
        hero_page = TheInternetHeroPage(self.driver)
        hero_page.select_list_item('Dropdown')

        Verify.true(hero_page.is_page_displayed("Dropdown List"), "Page isn't displayed")

        hero_page.set_dropdown_value(option_set_value)

        Verify.equals(hero_page.get_selected_value(), option_set_value, "Option isn't displayed")

    @pytest.mark.usefixtures("base_driver_setup_the_internet")
    def test_changing_dom(self):
        hero_page = TheInternetHeroPage(self.driver)
        hero_page.select_list_item('Challenging DOM')

        Verify.true(hero_page.is_page_displayed("Challenging DOM"), "Page isn't displayed")

        first_run = hero_page.get_button_names()
        hero_page.select_button_by_name(first_run[2])
        second_run = hero_page.get_button_names()

        Verify.not_equals(first_run, second_run, "Buttons aren't changed")

        hero_page.find_item_in_table("Definiebas1")
        hero_page.find_table_action("1", "delete")



