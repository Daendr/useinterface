from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.elements.text_box import TextBox
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.link import Link
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.combo_box import ComboBox
from tests.resources.emailGenerator import EmailGenerator
from tests.resources.passwordGenerator import PasswordGenerator


class GamePage(Form):
    __email = EmailGenerator.generate_email()
    __domain = EmailGenerator.generate_domain()
    __password = PasswordGenerator.generate_password(__email)

    __EmailTxbXpath: str = "//*[@placeholder='Your email']"
    __DomainTxbXpath: str = "//*[@placeholder='Domain']"
    __PasswordTxbXpath: str = "//*[@placeholder='Choose Password']"
    __DropdownCmbXpath: str = "//*[@class='dropdown__list-item'][1]"

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
        self.dropdown_opener = ComboBox(
            Locator(By.CLASS_NAME, "dropdown__opener"),
            "dropdown_opener")
        self.dropdown_dot_com = ComboBox(
            Locator(By.XPATH, self.__DropdownCmbXpath),
            "dropdown_dot_com")

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

    def select_dot_org(self):
        """Выбираем из dropbox .com"""
        self.dropdown_opener.click()
        self.dropdown_dot_com.click()
        # assert self.dropdown_dot_com.js_actions.get_selected_text() == ".org"
