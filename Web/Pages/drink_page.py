
import allure
from Web.Locators.drink_locators import Drink_Locators


from Web.Pages.utilities import Utilities


class DrinkPage(Utilities, Drink_Locators):
    @allure.step("option open")
    def select_option1(self, option1):
        self._click(option1)

    @allure.step("option to open")
    def select_the_option2(self, option2):
        self._click(option2)

    @allure.step("click to open the button")
    def save_click(self, save):
        self._click(save)

    @allure.step("Verify the color of font ")
    def color(self, location):
        element = self._find(location).value_of_css_property("background-color")

    @allure.step("Verify the clickable of drink button")
    def click_on_drink(self):
        self._click(self.drink)

    @allure.step("Verify the font size of the letter")
    def check_font_size_drink(self, location):
        self._find(location).value_of_css_property("font-size")

    @allure.step("Verify the font weight of the letter")
    def check_font_weight(self, location):
        self._find(location).value_of_css_property("font-weight")

    @allure.step("Verify the google button to open of ")
    def check_disply_pag(self, loctor):
        payment_page = self._find(loctor).get_attribute("page-google")

    @allure.step("Verify the font text of the letter")
    def check_text_alignment(self, location):
        self._find(location).value_of_css_property("text-align")



