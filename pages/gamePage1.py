from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.elements.label import Label
from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from utilities.passwordGenerator import PasswordGenerator
from py_selenium_auto.elements.button import Button


class GamePage1(Form):

    _email_text_box: TextBox = TextBox(
        Locator(By.XPATH, "//*[@placeholder='Your email']"),
        "email")
    _domain_text_box: TextBox = TextBox(
        Locator(By.XPATH, "//*[@placeholder='Domain']"),
        "domain")
    _password_text_box: TextBox = TextBox(
        Locator(By.XPATH, "//*[@placeholder='Choose Password']"),
        "password")
    _terms_label_agree: Label = Label(
        Locator(By.CLASS_NAME, "checkbox__box"),
        "terms_label_agree")
    _open_dropdown: Label = Label(
        Locator(By.CLASS_NAME, "dropdown__header"),
        "open_dropdown")
    _dropdown_list: Label = Label(
        Locator(By.XPATH, "//*[@class='dropdown__list-item']"),
        "dropdown_list")
    _next_btn: Button = Button(
        Locator(By.CLASS_NAME, "button--secondary"),
        "next_btn")


    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "login-form__terms-conditions"),
            "Проверка для 1 карточки",
        )

    def send_email(self, email):
        self._email_text_box.clear()
        self._email_text_box.send_keys(email)

    def send_domain(self, domain):
        self._domain_text_box.clear()
        self._domain_text_box.send_keys(domain)

    def send_password(self, email):
        password = PasswordGenerator.generate_password(email)
        self._password_text_box.clear()
        self._password_text_box.send_keys(password)

    def click_open_dropdown(self):
        self._open_dropdown.click()

    def select_high_domain(self):
        new_locator = BrowserServices.Instance.browser.driver.find_elements(By.XPATH, self._dropdown_list.locator.value)
        new_locator.click()

    def agree_terms(self):
        self._terms_label_agree.click()

    def click_next_btn(self):
        self._next_btn.click()
