import pytest
from py_selenium_auto_core.logging.logger import Logger
from pages.TheGamePage import GamePage
from pages.TheStartPage import StartPage


class Userinterface:

    @staticmethod
    @pytest.mark.test_Registration
    def test_Registration():
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        start_page.open()

        Logger.info("Шаг 2. Кликнуть по ссылке (в тексте 'Please click HERE to GO to the next page')"
                    " для перехода на следующую страницу.")
        start_page.click_here_link()

        Logger.info("Шаг 3. Введите случайные действующий пароль,"
                    " адрес электронной почты,примите условия пользования и нажмите кнопку 'Next'")
        game_page = GamePage()
        game_page.assert_cart_number()
        game_page.send_email()
        game_page.send_domain()
        game_page.send_password()
        game_page.select_dot_smth()
        game_page.agree_terms()
        game_page.click_next_btn()

        Logger.info("Шаг 4. Выберите 2 случайных интереса, загрузите изображение, нажмите кнопку 'Next'")
        game_page.upload_photo()
        game_page.choise_3_check_boxes()
        game_page.click_next_btn_on_second_card()

    @staticmethod
    @pytest.mark.test_Hide_help_form
    def test_Hide_help_form():

        """1. Перейти на домашнюю страницу."""
        start_page = StartPage()
        start_page.open()
        start_page.click_here_link()

        """2. Скрыть форму помощи."""
        game_page = GamePage()
        game_page.click_next_btn_with_wait()

    @staticmethod
    @pytest.mark.test_Accept_cookies
    def test_Accept_cookies():
        """1. Перейти на домашнюю страницу."""
        start_page = StartPage()
        start_page.open()
        start_page.click_here_link()

        """2. Принять cookies."""
        game_page = GamePage()
        game_page.click_accept_cookies()

    @staticmethod
    @pytest.mark.test_Timer
    def test_Timer():
        """1. Перейти на домашнюю страницу."""
        start_page = StartPage()
        start_page.open()
        start_page.click_here_link()

        game_page = GamePage()
        game_page.check_timer_starts_with_zero()
