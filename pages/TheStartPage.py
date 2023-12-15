from py_selenium_auto.browsers.browser_services import BrowserServices
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.link import Link
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class StartPage(Form):
    _base_url: str = "https://userinyerface.com/"

    def __init__(self):
        super().__init__(
            Locator(By.CLASS_NAME, "start__paragraph"),
            "Start Page",
        )
        self.here_link: Link = Link(
            Locator(By.CLASS_NAME, "start__link"),
            "HERE",
        )

    def open(self):
        """Открывает домашнюю страницу и ожидает её загрузки."""
        start_page = StartPage()

        BrowserServices.Instance.browser.go_to(self._base_url)
        BrowserServices.Instance.browser.wait_for_page_to_load()
        BrowserServices.Instance.browser.maximize()
        assert start_page.state.is_displayed(), "Start page should be displayed"

    def click_here_link(self):
        """Нажимаем Here"""
        self.here_link.click()
