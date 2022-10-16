from selenium.webdriver.common.by import By

from assertions.assertions import Assertions
from pages.base_page import BasePage


class ApiDocsPage(BasePage):
    """
    PageObject: https://timeapi.io/swagger/index.html'.

    """

    path = '/swagger/index.html'

    time_get_zone = (By.CSS_SELECTOR, "#operations-Time-get_api_Time_current_zone .opblock-summary-method")
    global_try_it_now_btn = (By.CSS_SELECTOR, ".try-out__btn.btn")

    def click_to_endpoint_by_locator(self, locator):
        self._click(*locator)

    def check_web_element_text(self, locator, text):
        element_text = self._get_web_element_text(*locator)
        Assertions.is_equal(element_text, text)
