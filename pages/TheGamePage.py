import random
import os
import pyautogui
import time
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.elements.element_factory import ElementFactory
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.elements.label import Label
from py_selenium_auto_core.elements.constants.element_state import ElementState
from py_selenium_auto_core.elements.constants.elements_count import ElementsCount
from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.combo_box import ComboBox
from utilities.emailGenerator import EmailGenerator
from utilities.indexGenerator import IndexGenerator
from utilities.passwordGenerator import PasswordGenerator
from py_selenium_auto.elements.element import Element
from py_selenium_auto.elements.button import Button
import subprocess
import time
from pygetwindow import getWindowsWithTitle

class GamePage(Form):
    __email = EmailGenerator.generate_email()
    __domain = EmailGenerator.generate_domain()
    __password = PasswordGenerator.generate_password(__email)

    __EmailTxbXpath: str = "//*[@placeholder='Your email']"
    __DomainTxbXpath: str = "//*[@placeholder='Domain']"
    __PasswordTxbXpath: str = "//*[@placeholder='Choose Password']"
    __DropdownCortForIndexGenerator = (By.CLASS_NAME, "dropdown__list-item")

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
        file_name = "avatar.png"
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        self.load_button.click()
        self.upload_button.click()
        # Запускаем AutoIt скрипт
        subprocess.Popen(["autoit3", "choose_file.au3"])

        # Ждем, пока окно выбора файла закроется
        while getWindowsWithTitle("Open"):
            time.sleep(1)