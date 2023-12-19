import pytest
from py_selenium_auto_core.logging.logger import Logger
from pages.TheStartPage import StartPage
from pages.gamePage1 import GamePage1
from pages.gamePage2 import GamePage2
from pages.gamePage3 import GamePage3
from pages.gamePageCookieForm import GamePageCookieForm
from pages.gamePageHelpForm import GamePageHelpForm
from pages.gamePageTimer import GamePageTimer
from utilities.generateRandomText import GenerateRandomText


class TestUserinterface:

    @staticmethod
    @pytest.mark.test_Registration
    def test_registration(setup_session):
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        assert start_page.state.is_displayed(), "Стартовая страница не отображена"

        Logger.info("Шаг 2. Кликнуть по ссылке (в тексте 'Please click HERE to GO to the next page')"
                    " для перехода на следующую страницу.")
        start_page.click_here_link()
        game_page_1 = GamePage1()
        assert game_page_1.state.is_displayed(), "Cтраница 1 карточки игры не отображена"

        Logger.info("Шаг 3. Введите случайные действующий пароль,"
                    " адрес электронной почты,примите условия пользования и нажмите кнопку 'Next'")
        email = GenerateRandomText.generate_random_text(10)
        game_page_1.send_email(email)
        game_page_1.send_domain(GenerateRandomText.generate_random_text(5))
        game_page_1.send_password(email)
        game_page_1.select_high_domain_in_dropdown()
        game_page_1.agree_terms()
        game_page_1.click_next_btn()
        game_page_2 = GamePage2()
        assert game_page_2.state.is_displayed(), "Cтраница 2 карточки игры не отображена"

        Logger.info("Шаг 4. Выберите 2 случайных интереса, загрузите изображение, нажмите кнопку 'Next'")
        game_page_2.upload_photo()
        game_page_2.click_checkbox_unselectall()
        game_page_2.click_random_checkboxes(3)
        game_page_2.click_next_btn_on_second_card()
        game_page_3 = GamePage3()
        assert game_page_3.state.is_displayed(), "Cтраница 3 карточки игры не отображена"

    @staticmethod
    @pytest.mark.test_Hide_help_form
    def test_hide_help_form(setup_session):
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        assert start_page.state.is_displayed(), "Стартовая страница не отображена"

        Logger.info("2. Скрыть форму помощи.")
        start_page.click_here_link()
        game_page_1 = GamePage1()
        assert game_page_1.state.is_displayed(), "Cтраница 1 карточки игры не отображена"

        game_page_help_form = GamePageHelpForm()
        game_page_help_form.click_next_btn()
        assert game_page_help_form.state.wait_for_not_displayed(), "Форма не исчезла после нажатия кнопки Next"

    @staticmethod
    @pytest.mark.test_Accept_cookies
    def test_accept_cookies(setup_session):
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        assert start_page.state.is_displayed(), "Стартовая страница не отображена"

        Logger.info("2. Принять cookies.")
        start_page.click_here_link()
        game_page_1 = GamePage1()
        assert game_page_1.state.is_displayed(), "Cтраница 1 карточки игры не отображена"

        game_page_cookie_form = GamePageCookieForm()
        game_page_cookie_form.click_accept_cookies()
        assert game_page_cookie_form.state.wait_for_not_displayed(),\
            "Форма не исчезла после нажатия на кнопку No, really no"

    @staticmethod
    @pytest.mark.test_Timer
    def test_timer(setup_session):
        Logger.info("Шаг 1. Перейти на домашнюю страницу.")
        start_page = StartPage()
        start_page.click_here_link()

        game_page_timer = GamePageTimer()
        game_page_timer.check_timer_starts_with_zero()
