import allure
import pytest
from Web.Pages.drink_page import DrinkPage
from Web.BasePage.basepage import BasePage


class Test_Drink(DrinkPage, BasePage):
    def handling_pop_up(self):
        self.open()
        self.select_option1(self.option1)
        self.select_the_option2(self.option2)
        self.save_click(self.save)

    @allure.description("verification of drink")
    def test_drink(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._driver.close()

    @allure.description("verification of drink font_of_drink")
    def test_font_of_drink(self):
        self.handling_pop_up()
        assert self.check_font_size_drink(self.drink_text) is None
        self._driver.close()

    @allure.description("Verification of drink color_text")
    def test_verify_color_of_drink_text(self):
        self.handling_pop_up()
        self.click_on_drink()
        assert self.color(self.drink_english_text) is None
        self._driver.close()

    @allure.description("Verification of drink name_text")
    def test_verify_list_of_name_of_drink_text(self):
        self.handling_pop_up()
        self.click_on_drink()
        assert self.check_text_alignment(self.milk) is None
        self._driver.close()

    @allure.description("Verification of drink currency_text")
    def test_verify_list_of_currency_of_drink_text(self):
        self.handling_pop_up()
        self.click_on_drink()
        assert self.check_text_alignment(self.currency) is None
        self._driver.close()

    @allure.description("Verification add_list_of_currency_of_drink_text")
    def test_verify_add_list_of_currency_of_drink_text(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        assert self._is_displayed(self.display_list)
        self._driver.close()

    @allure.description("Verification add_list_button_of_drink_list")
    def test_verify_add_list_button_of_drink_list(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        assert self._is_displayed(self.add_list_disply)
        self._driver.close()

    @allure.description("Check deleted_button_list_button_of_drink_list")
    def test_verify_deleted_button_list_button_of_drink_list(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        assert self._is_displayed(self.add_list_disply)
        self._click(self.deleted_button)
        assert self._is_displayed(self.empty_list)
        self._driver.close()

    @allure.description("Check minus_list_button_of_drink_list")
    def test_verify_minus_list_button_of_drink_list(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.mianes_button)
        assert self._is_displayed(self.empty_list)
        self._driver.close()

    @allure.description("Check pyment_list_of_currency_of_drink_text")
    def test_verify_add_pyment_list_of_currency_of_drink_text(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        assert self._is_displayed(self.pyment_page)
        self._driver.close()

    @allure.description("Check X_button_pyment_click")
    def test_verify_X_button_pyment_click(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        assert self._is_displayed(self.pyment_page)
        self._click(self.x_button)
        assert self._is_displayed(self.add_button)
        self._driver.close()

    @allure.description("Check goole_signin_pyment_click")
    def test_verify_goole_signin_pyment_click(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        self._click(self.signin)
        self._click(self.google_button)
        display_google_page = self._click(self.signin_button)
        assert display_google_page == "will come to google payment page"
        self._driver.close()

    @allure.description("Check facebook_signin_pyment_click")
    def test_verify_facebook_signin_pyment_click(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        self._click(self.signin)
        self._click(self.facebook_button)
        display_facebook_page = self._click(self.signin_button)
        assert display_facebook_page == "will come to facebook payment page"
        self._driver.close()

    @allure.description("Check tweeter_signin_pyment_click")
    def test_verify_tweeter_signin_pyment_click(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        self._click(self.signin)
        self._click(self.tweeter_button)
        display_tweeter_page = self._click(self.signin_button)
        assert display_tweeter_page == "will come to tweeter payment page"
        self._driver.close()

    @allure.description("Check goole_signin_pyment_click")
    def test_verify_goole_signup_pyment_click(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        self._click(self.signup_registor_button)
        self._click(self.google_button)
        display_google_page = self._click(self.signin_button)
        assert display_google_page == "will come to google payment page"
        self._driver.close()

    @allure.description("Check facebook_signin_pyment_click")
    def test_verify_facebook_signup_pyment_click(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        self._click(self.signup_registor_button)
        self._click(self.facebook_button)
        display_facebook_page = self._click(self.signin_button)
        assert display_facebook_page == "will come to facebook payment page"
        self._driver.close()

    @allure.description("Check tweeter_signin_pyment_click")
    def test_verify_tweeter_signup_pyment_click(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        self._click(self.signup_registor_button)
        self._click(self.tweeter_button)
        display_tweeter_page = self._click(self.signin_button)
        assert display_tweeter_page == "will come to tweeter payment page"
        self._driver.close()

    @allure.description("Check without_phone_number_signup_pyment_click")
    def test_verify_without_phone_number_signup_pyment_click(self):
        self.handling_pop_up()
        self.click_on_drink()
        self._click(self.addcart)
        self._click(self.add_button)
        self._click(self.pyment)
        display_tweeter_page = self._click(self.phone_filed)
        self._click(self.signup_registor_button)

        assert display_tweeter_page == "will come to fill out "
        self._driver.close()
