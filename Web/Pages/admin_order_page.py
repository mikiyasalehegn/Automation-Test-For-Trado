from datetime import time

import allure
from selenium.webdriver.common.by import By

from Web.Locators.admin_order_locator import *

from Web.Pages.utilities import Utilities


class AdminPage(Utilities, admail_loctore):

    @allure.step
    def enter_phone_fild(self):
        self._find(self.Phone_contact).send_keys("1953333333")

    @allure.step
    def enter_invalid_phone_fild(self):
        self._find(self.Phone_contact).send_keys("195333333")

    @allure.step
    def enter_empty_phone_fild(self):
        self._find(self.Phone_contact).send_keys("")

    @allure.step
    def click_submit_button(self, locator):
        self._click(locator)

    @allure.step
    def enter_code_fild(self):
        self._find(self.Code_contact).send_keys("1234")

    @allure.step
    def enter_invalid_code_fild(self):
        self._find(self.Code_contact).send_keys("1233")

    @allure.step
    def enter_empty_code_fild(self):
        self._find(self.Code_contact).send_keys("")

    @allure.step
    def enter_letter_code_fild(self):
        self._find(self.Code_contact).send_keys("team")

    @allure.step
    def enter_search_fild(self):
        self._find(self.Code_contact).send_keys("edaws")
