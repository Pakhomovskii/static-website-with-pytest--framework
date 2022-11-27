import logging
import pytest
from page_objects.main_page_check import MainPage
from tests.base_test import BaseTest

logger = logging.getLogger(__name__)


class TestVisibility(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = MainPage(self.driver, self.wait)
        self.page.go_to_search_page()

    def test_header_block(self, load_pages):
        self.page.check_header_block()
