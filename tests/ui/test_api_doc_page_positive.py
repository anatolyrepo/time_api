import pytest

from configs.config import Config
from pages.api_docs_page import ApiDocsPage
from suite.base import BaseUiTestClass


@pytest.mark.api_docs
class TestApiDocPage(BaseUiTestClass):

    def test_get_api_docs_page_success(self):
        """Проверка получения страницы Api Docs."""

        self.get_page(ApiDocsPage)
        self.assertions.is_equal(Config.base_url + ApiDocsPage.path, self.browser.current_url)

    def test_check_page_title_success(self):
        """Проверка получения страницы Api Docs."""

        self.get_page(ApiDocsPage)
        self.assertions.is_equal(self.browser.title, "Time API")

    def test_time_zone_try_it_now_is_present_success(self):
        """Проверка получения страницы Api Docs."""

        api_doc_page = self.get_page(ApiDocsPage)
        api_doc_page.
