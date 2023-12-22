from selenium.webdriver.common.by import By
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class GamePage3(Form):
    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "personal-details__td-label"),
            "Проверка для 3 карточки",
        )
