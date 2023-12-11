import abc

from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.forms.form import Form
from selenium.webdriver.common.by import By


class TheHomePage(Form):
    _base_url: str = "https://userinyerface.com/"

    def __init__(self, locator: Locator, name: str):
        super().__init__(locator, name)

    fake_element = Locator(By.XPATH, "//fake")
    timeout = 1
    element_factory = BrowserServices.Instance.service_provider.element_factory()
    element_factory.get_button(fake_element, "Fake").get_element(timeout)

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
