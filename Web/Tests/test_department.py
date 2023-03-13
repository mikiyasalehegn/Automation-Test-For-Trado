import time

import allure
import pytest
from Web.Data.data4 import Data4
from Web.Pages.department_page import DepartmentPage


class Test_Department(DepartmentPage, Data4):

    def handling_the_first_popup(self):
        self.open_admin()
        self.select_enter_code(self.option_Phone, "1953333333")
        self.click_button()
        time.sleep(3)
        self.enter_phone_valid(self.field_code, "1234")
        time.sleep(2)
        self.select_button()

    @allure.description("Test Department clickable correctly ")
    def test_department_button_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._driver.close()

    @allure.description("Test Department name is displayed all the name of the users name correctly ")
    def test_department_name_displayed(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_name_displayed()
        self._driver.close()

    def test_department_name_arrow_displayed(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_images()
        self._driver.close()

    @allure.description("Test The Department image clickable correctly ")
    def test_department_name(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_cover_image()
        self._driver.close()

    @allure.description("Test the Department active title is clickable correctly ")
    def test_department_active(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_active()
        self._driver.close()

    @allure.description("Test the Department CrateArt title is clickable correctly ")
    def test_department_creatart(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_creatart()
        self._driver.close()

    @allure.description("Test the Department three dots of button is displayed correctly ")
    def test_department_three_dots(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_three_dots()
        self._driver.close()

    @allure.description("Test the up and down line is working properly")
    def test_department_up_down(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_up_down()
        self._driver.close()

    @allure.description("Test Department add button verify the correct data")
    def test_department_up_down(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_three_dots()
        self.department_plus_add()
        self._driver.close()

    @allure.description("Test Department add button verify correct data")
    def test_department_up_down(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_three_dots()
        self.department_plus_add()
        self._driver.close()

    @allure.description("Test Department export button verify correct data")
    def test_department_export(self):
        self.handling_the_first_popup()
        self.click_contents()
        self.department_three_dots()
        self.department_export()
        self._driver.close()

    @allure.description("Test Department the name of the users data verify correctly")
    def test_department_export(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.name_user)
        assert self.name_user == ('xpath', '//tbody/tr[1]/td[2]')
        self.department_update_button()
        self._driver.close()

    @allure.description("Test the Department categories of auto save button is clikable correctly")
    def test_department_auto_save_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.name_user)
        self._click(self.auto_on)
        self._driver.close()

    @allure.description("Test the Department categories of 'x' is clikable correctly")
    def test_department_auto_save_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.name_user)
        self._click(self.x)
        self._driver.close()

    @allure.description("Test the Department categories of 'Department' title is aligned correctly")
    def test_department_auto_save_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.name_user)
        self._is_displayed(self.text_displyed)
        assert self.text_displyed == ('xpath', "//span[contains(text(),'מחלקה')]")
        self._driver.close()

    @allure.description("Test the Department categories of 'Search' box is clikable")
    def test_department_auto_save_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.search_input)
        self._driver.close()

    @allure.description("Test the Department categories of 'Search' box is working correctly")
    def test_department_auto_save_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.search_input)
        assert self.search_input == ('xpath',
                                     "//body/div[@id='root']/div[1]/div[2]/main"
                                     "[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]")
        self._driver.close()

    @allure.description("Test the Department categories of the Three line description is working correctly")
    def test_department_auto_save_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.three_line_menu)
        self._driver.close()

    @allure.description("Test the Department categories of the Total row value is aligned correctly")
    def test_department_auto_save_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.three_line_menu)
        self.text_reading(self.total_rows)
        self._driver.close()

    @allure.description("Test the Department categories of the Total row value is aligned correctly")
    def test_department_auto_save_clickable(self):
        self.handling_the_first_popup()
        self.click_contents()
        self._click(self.three_line_menu)
        self.text_reading(self.total_rows)
        self._click(self.open_page_limit)
        self._driver.close()





