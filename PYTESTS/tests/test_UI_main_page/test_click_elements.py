import logging
import pytest
from page_objects.main_page_check import MainPage
from tests.base_test import BaseTest

logger = logging.getLogger(__name__)


class TestClick(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = MainPage(self.driver, self.wait)
        self.page.go_to_search_page()

    def test_click_footer_elements(self, load_pages):

        logger.info("Check clickable footer links...")
        self.page.check_footer()

