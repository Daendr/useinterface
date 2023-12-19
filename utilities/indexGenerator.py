import random
from py_selenium_auto.browsers.browser_services import BrowserServices
from selenium.webdriver.common.by import By
from py_selenium_auto_core.logging.logger import Logger


class IndexGenerator:

    @staticmethod
    def generate_locator(elem_class):
        Logger.info("Метод который генерирует элемент")
        elements = BrowserServices.Instance.browser.driver.find_elements(By.CLASS_NAME, elem_class.locator.value)
        filtered_elements = [element for element in elements if "selected" not in element.get_attribute("class")]
        selected_element = random.choice(filtered_elements)
        return selected_element
