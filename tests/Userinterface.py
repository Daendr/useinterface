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
    @pytest.mark.test1
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
        game_page.click_next_btn()

        """4. Выберите 2 случайных интереса, загрузите изображение, нажмите кнопку 'Next'"""
        game_page.upload_photo()
        game_page.choise_3_check_boxes()
        game_page.click_next_btn_on_second_card()

    @staticmethod
    @pytest.mark.test2
    def test_case_2():

        """1. Перейти на домашнюю страницу."""
        start_page = StartPage()
        start_page.open()
        start_page.click_here_link()

        """2. Скрыть форму помощи."""
        game_page = GamePage()
        game_page.click_next_btn_with_wait()

    @staticmethod
    @pytest.mark.test3
    def test_case_3():
        """1. Перейти на домашнюю страницу."""
        start_page = StartPage()
        start_page.open()
        start_page.click_here_link()

        """2. Принять cookies."""
        game_page = GamePage()
        game_page.click_accept_cookies()

    @staticmethod
    @pytest.mark.test4
    def test_case_4():
        """1. Перейти на домашнюю страницу."""
        start_page = StartPage()
        start_page.open()
        start_page.click_here_link()

        game_page = GamePage()
        game_page.check_timer_starts_with_zero()

