import pytest
from py_selenium_auto.browsers.browser_services import BrowserServices

from pages.TheStartPage import StartPage


class TestUI:
    @staticmethod
    def teardown_method():
        if BrowserServices.Instance.is_browser_started:
            BrowserServices.Instance.browser.quit()
    @staticmethod
    @pytest.mark.test
    def test_case_1():
        """1. Перейти на домашнюю страницу."""
        start_page = StartPage()
        start_page.open()


        """2. Кликнуть по ссылке (в тексте "Please click HERE to GO to the next page") для перехода на следующую страницу."""
        start_page.click_here_link()


        """Закрываем браузер"""
        TestUI.teardown_method()

