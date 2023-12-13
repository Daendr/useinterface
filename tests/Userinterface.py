import time

import pytest
from py_selenium_auto.browsers.browser_services import BrowserServices
from pages.TheGamePage import GamePage
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

        """2. Кликнуть по ссылке (в тексте "Please click HERE to GO to the next page")
        для перехода на следующую страницу."""
        start_page.click_here_link()

        """3. Введите случайные действующий пароль, адрес электронной почты, 
        примите условия пользования и нажмите кнопку "Next"""
        game_page = GamePage()
        game_page.assert_cart_number()
        game_page.send_email()
        game_page.send_domain()
        game_page.send_password()
        game_page.select_dot_smth()
        game_page.agree_terms()

        """Закрываем браузер"""
        TestUI.teardown_method()

