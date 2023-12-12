import abc

from py_selenium_auto.browsers.browser_services import BrowserServices
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.link import Link
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.check_box import CheckBox
from py_selenium_auto.elements.label import Label
from py_selenium_auto.elements.text_box import TextBox


class TheInternetForm(Form):
    _base_url: str = "https://the-internet.herokuapp.com/"

    def __init__(self, locator: Locator, name: str):
        super().__init__(locator, name)
        self.elemental_selenium_link: Link = Link(
            Locator(By.XPATH, "//a[contains(@href,'elementalselenium')]"),
            "Elemental Selenium",
        )

    @property
    @abc.abstractmethod
    def _url_part(self) -> str:
        ...

    @property
    def url(self):
        return self._base_url + self._url_part

    def open(self):
        BrowserServices.Instance.browser.go_to(self.url)
        BrowserServices.Instance.browser.wait_for_page_to_load()


class DynamicControlsForm(TheInternetForm):
    def __init__(self):
        super().__init__(
            Locator(By.ID, "content"),
            "DynamicControls",
        )
        self.text_input_text_box = TextBox(Locator(By.XPATH, "//input[@type='text']"), "Text input")
        self.change_input_state_button = Button(
            Locator(By.XPATH, "//form[@id='input-example']//button"),
            "Change input state",
        )
        self.example_checkbox = CheckBox(
            Locator(By.XPATH, "//input[@type='checkbox']"),
            "Example checkbox",
        )
        self.remove_add_example_button = Button(
            Locator(By.XPATH, "//form[@id='checkbox-example']//button"),
            "Remove\\Add example checkbox",
        )
        self.loading_label = Label(
            Locator(By.ID, "loading"),
            "Loading",
        )

    @property
    def _url_part(self) -> str:
        return "dynamic_controls"


class StartPage(Form):
    form = DynamicControlsForm()
    _base_url: str = "https://userinyerface.com/"
    element_selector = "p.start__paragraph"

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "start__link"),
            "Start Page",
        )
        self.here_link: Link = Link(
            Locator(By.CLASS_NAME, "start__link"),
            "HERE",
        )

    @property
    def _url_part(self) -> str:
        return ""

    def open(self):
        """Открывает домашнюю страницу и ожидает её загрузки."""
        BrowserServices.Instance.browser.go_to(self._base_url + self._url_part)
        BrowserServices.Instance.browser.wait_for_page_to_load()
        BrowserServices.Instance.browser.maximize()

    def click_here_link(self):
        self.here_link.click()

    def test_check_exist_element_state(self):
        self.form.change_input_state_button.click()
        assert self.form.loading_label.state.is_exist(), "Loading element should not exist after changing state"

# @property
#     def _url_part(self) -> str:
#         return "dynamic_controls"
#
#     def test_check_exist_element_state(self):
#         self.change_input_state_button.click()
#         assert self.is_element_present(self.loading_label), "Loading element should not exist after changing state"