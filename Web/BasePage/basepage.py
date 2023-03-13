import allure
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class BasePage:
    _driver = webdriver.Chrome()

    def _find(self, locate) -> WebElement:
        self._wait_until_element_is_visible(locate)
        return self._driver.find_element(*locate)

    def _entry(self, locate, content):
        self._wait_until_element_is_visible(locate)
        self._find(locate).clear()
        self._find(locate).send_keys(content)

    def _wait_until_element_is_visible(self, locate, time: int = 15):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locate))

    def scroll(self, locate, upto):
        self._wait_until_element_is_visible(locate)
        self._driver.execute_script(upto)

    def _click(self, locate):
        self._wait_until_element_is_visible(locate)
        self._find(locate).click()

    def _is_displayed(self, locate) -> bool:
        return self._find(locate).is_displayed()

    def _find_elements(self, locator):
        self._wait_until_element_is_visible(locator)
        return self._driver.find_elements(*locator)

    @allure.step("Opening the qa-trado website")
    def open(self):
        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self._driver.get("https://qa.trado.co.il/")
        self._driver.maximize_window()

    def text_reading(self, locate):
        return self._find(locate).text

    def read_alert(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.alert_is_present())
        return self._driver.switch_to.alert.text

    def _select(self, locate, val):
        date = Select(self._find(locate))
        date.select_by_value(val)

    @allure.step("Opening the qa-trado website")
    def open_admin(self):
        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self._driver.get("https://qa-admin.trado.co.il/")
        self._driver.maximize_window()

    @allure.step
    def _is_enabled(self, locator):
        self._wait_until_element_is_visible(locator)
        self._driver.find_element(*locator).is_enabled()


