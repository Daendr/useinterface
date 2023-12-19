import locale
import os
import random
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.elements.label import Label
from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.button import Button
import subprocess


class GamePage2(Form):
    _open_dropdown: Label = Label(
        Locator(By.CLASS_NAME, "dropdown__header"),
        "open_dropdown")
    _dropdown_list_xpath: Label = Label(
        Locator(By.XPATH, "//*[@class='dropdown__list-item']"),
        "dropdown_list")
    _dropdown_list_class: Label = Label(
        Locator(By.CLASS_NAME, "dropdown__list-item"),
        "dropdown_list")
    _next_btn: Button = Button(
        Locator(By.CLASS_NAME, "button--secondary"),
        "next_btn")
    _dropdown_list_xpath_1: Label = Label(
        Locator(By.XPATH, "//*[@class='dropdown__list-item'][1]"),
        "dropdown_list")
    _upload_button: Button = Button(
        Locator(By.CLASS_NAME, "avatar-and-interests__upload-button"),
        "upload_button")
    _load_button: Button = Button(
        Locator(By.XPATH, "//*[contains(text(), 'Download image')]"),
        "load_button")
    _next_button_2_card: Button = Button(
        Locator(By.XPATH, "//*[contains(text(), 'Next')]"),
        "next_button_2_card")
    _check_boxes_element: Label = Label(
        Locator(By.CLASS_NAME, "avatar-and-interests__interests-list__item"),
        "check_boxes_element")
    _check_boxes_label: Label = Label(
        Locator(By.CLASS_NAME, "checkbox__label"),
        "check_boxes_label")
    _unselectall_checkboxes: Button = Button(
        Locator(By.XPATH, f'//*[@for="interest_unselectall"]'),
        "_unselectall_checkboxes")

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "avatar-and-interests__title"),
            "Проверка для 2 карточки",
        )

    def upload_photo(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        system_language, _ = locale.getdefaultlocale()
        if system_language.startswith('ru'):
            autoit_script = "choose_file_ru.exe"
        else:
            autoit_script = "choose_file_en.exe"
        autoit_exe_path = os.path.join(script_dir, "../utilities", autoit_script)
        self._upload_button.click()
        subprocess.run([autoit_exe_path])

    def click_checkbox_unselectall(self):
        self._unselectall_checkboxes.click()

    @staticmethod
    def click_random_checkboxes(num):
        checkbox_list = BrowserServices.Instance.browser.driver.find_elements(
            By.XPATH, f"//label[not(@for='interest_unselectall' or @for='interest_selectall')]")
        for _ in range(num):
            random_checkbox = random.choice(checkbox_list)
            random_checkbox.click()
            checkbox_list.remove(random_checkbox)

    def click_next_btn_on_second_card(self):
        self._next_button_2_card.click()
