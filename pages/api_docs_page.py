from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from assertions.assertions import Assertions


class ApiDocsPage(BasePage):
    """
    PageObject: https://timeapi.io/swagger/index.html'.

    """

    path = '/swagger/index.html'

    time_get_zone = (By.CSS_SELECTOR, "#operations-Time-get_api_Time_current_zone .opblock-summary-method")
    global_try_it_now_btn = (By.CSS_SELECTOR, ".try-out__btn.btn")

    def go_to_full_info(self, locator):
        self._click(*locator)

    def assert_web_element_text(self, locator, text):
        element_text = self._get_web_element_text(*locator)
        Assertions.is_equal(element_text, text)
