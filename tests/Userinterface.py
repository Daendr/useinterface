from py_selenium_auto.browsers.browser_services import BrowserServices


class UserInterface:

    @staticmethod
    def teardown_method():
        if BrowserServices.Instance.is_browser_started:
            BrowserServices.Instance.browser.quit()
