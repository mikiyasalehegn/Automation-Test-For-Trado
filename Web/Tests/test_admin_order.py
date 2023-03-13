import time

import allure

from Web.Pages.admin_order_page import AdminPage


class Test_admin_page_open(AdminPage):

    @allure.description('Navigate to admin order page')
    def test_admin_order_click(self):
        self.open_admin()
        self.enter_phone_fild()
        self.click_submit_button(self.Submit_button)
        time.sleep(4)
        self.enter_code_fild()
        self.click_submit_button(self.Sign_button)
        assert self._is_displayed(self.chak_page)
        self._driver.close()

    @allure.description('Navigate admin to order list page')
    def test_order_list_check(self):
        self.open_admin()
        self.enter_phone_fild()
        self.click_submit_button(self.Submit_button)
        time.sleep(3)
        self.enter_code_fild()
        self.click_submit_button(self.Sign_button)
        self.click_submit_button(self.oder_button)
        assert self._is_displayed(self.checkOrederPage)
        self._driver.close()

    @allure.description('Navigate admin to invalid_phone_number page')
    def test_enter_invalid_phone_number(self):
        self.open_admin()
        self.enter_invalid_phone_fild()
        time.sleep(3)
        self.click_submit_button(self.Submit_button)
        assert self._is_displayed(self.empty_fild)
        self._driver.close()

    @allure.description('Navigate admin to empty_phone_number page')
    def test_empty_phone_number(self):
        self.open_admin()
        self.enter_empty_phone_fild()
        time.sleep(3)
        self.click_submit_button(self.Submit_button)
        assert self._is_displayed(self.empty_fild)
        self._driver.close()

    @allure.description('Navigate admin to invalid_code_number page')
    def test_invalid_code(self):
        self.open_admin()
        self.enter_phone_fild()

        self.click_submit_button(self.Submit_button)
        self.enter_invalid_code_fild()
        time.sleep(3)
        self.click_submit_button(self.Sign_button)
        assert self._is_displayed(self.empty_fild)
        self._driver.close()

    @allure.description('Navigate admin to empty_code_number page')
    def test_empty_code(self):
        self.open_admin()
        self.enter_phone_fild()
        time.sleep(3)
        self.click_submit_button(self.Submit_button)
        self.enter_letter_code_fild()
        self.click_submit_button(self.Sign_button)
        assert self._is_displayed(self.empty_fild)
        self._driver.close()

    @allure.description('Navigate admin to last page')
    def test_last_page_check(self):
        self.open_admin()
        self.enter_phone_fild()
        self.click_submit_button(self.Submit_button)
        time.sleep(3)
        self.enter_code_fild()
        self.click_submit_button(self.Sign_button)
        self.click_submit_button(self.oder_button)
        self.click_submit_button(self.last_page_button)
        assert self._is_displayed(self.last_page)
        self._driver.close()

    @allure.description('Navigate admin Export_page_button_check page')
    def test_Export_page_button_check(self):
        self.open_admin()
        self.enter_phone_fild()
        self.click_submit_button(self.Submit_button)
        time.sleep(3)
        self.enter_code_fild()
        self.click_submit_button(self.Sign_button)
        self.click_submit_button(self.oder_button)
        assert self._is_displayed(self.export_button)
        self._driver.close()

    @allure.description('Navigate admin search_page_button_check page')
    def test_Search_page_check(self):
        self.open_admin()
        self.enter_phone_fild()
        self.click_submit_button(self.Submit_button)
        time.sleep(3)
        self.enter_code_fild()
        self.click_submit_button(self.Sign_button)
        self.click_submit_button(self.oder_button)
        self.click_submit_button(self.search_button)
        assert self._is_displayed(self.search_button)
        self._driver.close()

    @allure.description('Navigate admin search_button page')
    def test_list_search_page_check(self):
        self.open_admin()
        self.enter_phone_fild()
        self.click_submit_button(self.Submit_button)
        time.sleep(3)
        self.enter_code_fild()
        self.click_submit_button(self.Sign_button)
        self.click_submit_button(self.oder_button)
        self.click_submit_button(self.rady_order)
        assert self._is_displayed(self.list_oerder)
        self._driver.close()

    @allure.description('Navigate admin name_list_page_check page')
    def test_name_list_page_check(self):
        self.open_admin()
        self.enter_phone_fild()
        self.click_submit_button(self.Submit_button)
        time.sleep(3)
        self.enter_code_fild()
        self.click_submit_button(self.Sign_button)
        self.click_submit_button(self.oder_button)
        self.click_submit_button(self.list_rady)
        assert self._is_displayed(self.list_disply)
        self._driver.close()

    @allure.description('Navigate admin total_list_page_check page')
    def test_total_list_page_check(self):
        self.open_admin()
        self.enter_phone_fild()
        self.click_submit_button(self.Submit_button)
        time.sleep(3)
        self.enter_code_fild()
        self.click_submit_button(self.Sign_button)
        self.click_submit_button(self.oder_button)
        self.click_submit_button(self.total_result)
        assert self._is_displayed(self.sum_list)
        self._driver.close()
