from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная страница PageObject: https://timeapi.io.
    """

    path = '/'

    API_DOCS = (By.CSS_SELECTOR, ".navbar-nav .nav-item:nth-child(3) a")

    def go_to_api_doc_page(self):
        self._click(*self.API_DOCS)
