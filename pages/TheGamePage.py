import random

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
from utilities.passwordGenerator import PasswordGenerator
from py_selenium_auto.elements.element import Element


class GamePage(Form):
    __email = EmailGenerator.generate_email()
    __domain = EmailGenerator.generate_domain()
    __password = PasswordGenerator.generate_password(__email)

    __EmailTxbXpath: str = "//*[@placeholder='Your email']"
    __DomainTxbXpath: str = "//*[@placeholder='Domain']"
    __PasswordTxbXpath: str = "//*[@placeholder='Choose Password']"

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
        self.dropdown_list: Label = Label(
            Locator(By.CLASS_NAME, "dropdown__list-item"),
            "dropdown_list")

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
        dropdown_locator = Locator(By.CLASS_NAME, "dropdown__list")
        dropdown_elements = BrowserServices.Instance.browser.driver.find_elements(By.CLASS_NAME, "dropdown__list-item")
        # dropdown_elements = self.dropdown_list.finder.find_elements(
        #     locator=dropdown_locator,
        #     state=ElementState.Displayed,
        #     timeout=10,
        #     name="Dropdown List Items"
        # )
        dropdown_elements[1].click()

    def agree_terms(self):
        self.terms_label_agree.click()
