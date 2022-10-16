from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ApiDocsPage(BasePage):
    """
    PageObject: https://timeapi.io/swagger/index.html'.

    """

    path = '/swagger/index.html'

    time_get_zone = (By.CSS_SELECTOR, "#operations-Time-get_api_Time_current_zone .opblock-summary-method")
    try_it_now_btn = (By.CSS_SELECTOR, ".try-out__btn.btn")
