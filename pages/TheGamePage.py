import os
import time

from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.elements.label import Label
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from utilities.check_box_util import CheckBoxUtil
from utilities.emailGenerator import EmailGenerator
from utilities.indexGenerator import IndexGenerator
from utilities.passwordGenerator import PasswordGenerator
from py_selenium_auto.elements.button import Button
import subprocess


class GamePage(Form):
    __email = EmailGenerator.generate_email()
    __domain = EmailGenerator.generate_domain()
    __password = PasswordGenerator.generate_password(__email)

    __EmailTxbXpath: str = "//*[@placeholder='Your email']"
    __DomainTxbXpath: str = "//*[@placeholder='Domain']"
    __PasswordTxbXpath: str = "//*[@placeholder='Choose Password']"
    __DropdownCortForIndexGenerator = (By.CLASS_NAME, "dropdown__list-item")

    class_name_of_elements, class_name_of_element, unique_label, excluded_values = (
        "avatar-and-interests__interests-list__item",'checkbox__label', 'for',
        ['interest_unselectall', 'interest_selectall'])

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "login-form__terms-conditions"),
            "Карточка 1",
        )
        self.email_text_box: TextBox = TextBox(
            Locator(By.XPATH, self.__EmailTxbXpath),
            "email")
        self.domain_text_box: TextBox = TextBox(
            Locator(By.XPATH, self.__DomainTxbXpath),
            "domain")
        self.password_text_box: TextBox = TextBox(
            Locator(By.XPATH, self.__PasswordTxbXpath),
            "password")
        self.terms_label_agree: Label = Label(
            Locator(By.CLASS_NAME, "checkbox__box"),
            "terms_label_agree")
        self.open_dropdown: Label = Label(
            Locator(By.CLASS_NAME, "dropdown__header"),
            "open_dropdown")
        self.dropdown_list_xpath: Label = Label(
            Locator(By.XPATH, "//*[@class='dropdown__list-item']"),
            "dropdown_list")
        self.dropdown_list_class: Label = Label(
            Locator(By.CLASS_NAME, "dropdown__list-item"),
            "dropdown_list")
        self.next_btn: Button = Button(
            Locator(By.CLASS_NAME, "button--secondary"),
            "next_btn")
        self.dropdown_list_xpath_1: Label = Label(
            Locator(By.XPATH, "//*[@class='dropdown__list-item'][1]"),
            "dropdown_list")
        self.cart_number_assert: Label = Label(
            Locator(By.CLASS_NAME, "page-indicator"),
            "cart_number_assert")
        self.upload_button: Button = Button(
            Locator(By.CLASS_NAME, "avatar-and-interests__upload-button"),
            "upload_button")
        self.load_button: Button = Button(
            Locator(By.XPATH, "//*[contains(text(), 'Download image')]"),
            "load_button")
        self.next_button_2_card: Button = Button(
            Locator(By.XPATH, "//*[contains(text(), 'Next')]"),
            "next_button_2_card")
        self.help_form_btn: Button = Button(
            Locator(By.CLASS_NAME, "help-form__send-to-bottom-button"),
            "help_form_btn")
        self.accept_cookies: Label = Label(
            Locator(By.CLASS_NAME, "align__cell"),
            "accept_cookies")

    @staticmethod
    def assert_cart_number():
        """Проверяем нахождение на странице карточки 1."""
        game_page = GamePage()
        assert game_page.state.is_displayed(), "Game page should be displayed"

    def send_email(self):
        """Вставляем созданный email"""
        self.email_text_box.clear()
        self.email_text_box.send_keys(self.__email)
        assert self.email_text_box.value == self.__email

    def send_domain(self):
        """Вставляем созданный domain"""
        self.domain_text_box.clear()
        self.domain_text_box.send_keys(self.__domain)
        assert self.domain_text_box.value == self.__domain

    def send_password(self):
        """Вставляем созданный password"""
        self.password_text_box.clear()
        self.password_text_box.send_keys(self.__password)
        assert self.password_text_box.value == self.__password

    def select_dot_smth(self):
        """Выбираем из dropbox случайное значение"""
        self.open_dropdown.click()
        new_locator = IndexGenerator.generate_locator(self.dropdown_list_class, self.dropdown_list_xpath)
        new_locator.click()

    def agree_terms(self):
        """Снимаем галочку и принимаем соглашение"""
        self.terms_label_agree.click()

    def click_next_btn(self):
        """Нажимаем Next и assert на новую карточку"""
        self.next_btn.click()
        assert self.cart_number_assert.get_text() == '2 / 4'

    def upload_photo(self):
        """Скачиваем фото и отправляем на сервер"""
        # Получение пути к текущему каталогу скрипта Python
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Сборка относительного пути к исполняемому файлу AutoIt
        autoit_exe_path = os.path.join(script_dir, "..\\tests\\choose_file.exe")
        self.upload_button.click()
        subprocess.run([autoit_exe_path])

    def choise_3_check_boxes(self):
        # Использование метода для получения уникальных значений
        unique_values = CheckBoxUtil.get_unique_values_from_checkbox_labels(
            self.class_name_of_elements, self.class_name_of_element, self.unique_label)

        CheckBoxUtil.click_checkbox_by_for_value('interest_unselectall')
        CheckBoxUtil.click_random_checkboxes(unique_values, self.excluded_values)

    def click_next_btn_on_second_card(self):
        """Нажимаем Next и assert на новую карточку"""
        self.next_button_2_card.click()
        assert self.cart_number_assert.get_text() == '3 / 4'

    def click_next_btn_with_wait(self, timeout=15):
        """Нажимаем Next и assert на новую карточку"""
        self.help_form_btn.click()

        start_time = time.time()
        while True:
            if not self.help_form_btn.js_actions.is_element_on_screen():
                print("Элемент не видим.")
                break

            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                raise TimeoutException(f"Превышено время ожидания ({timeout} сек) для видимости элемента.")

            time.sleep(1)

        assert not self.help_form_btn.js_actions.is_element_on_screen(), "Форма не исчезла после нажатия кнопки Next"

    def click_accept_cookies(self):
        """Нажимаем Not really, no и делаем проверку на наличие элемента."""
        self.accept_cookies.click()
        time.sleep(5)
        assert not self.accept_cookies.js_actions.is_element_on_screen()
