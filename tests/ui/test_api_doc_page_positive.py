import pytest

from configs.config import Config
from pages.api_docs_page import ApiDocsPage
from suite.base import BaseUiTestClass


@pytest.mark.api_docs
class TestApiDocPage(BaseUiTestClass):

    def test_get_api_docs_page_success(self):
        """Проверка url страницы Api Docs."""

        self.get_page(ApiDocsPage)
        self.assertions.is_equal(Config.base_url + ApiDocsPage.path, self.browser.current_url)

    def test_check_page_title_success(self):
        """Проверка title страницы Api Docs."""

        self.get_page(ApiDocsPage)
        self.assertions.is_equal(self.browser.title, "Time API")

    def test_time_zone_text_try_it_out_success(self):
        """Проверка наличия текста "Try it out."""

        api_doc_page = self.get_page(ApiDocsPage)
        api_doc_page.click_to_endpoint_by_locator(api_doc_page.time_get_zone)
        api_doc_page.check_web_element_text(api_doc_page.global_try_it_now_btn, "Try it out")
