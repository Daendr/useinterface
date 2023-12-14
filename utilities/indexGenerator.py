import random
from py_selenium_auto.elements.label import Label
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class IndexGenerator:

    @staticmethod
    def generate_locator(elem_class, elem_xpath: Label):
        """Генерирует элемент"""
        cort = elem_class.locator
        cort_1 = elem_xpath.locator.value
        random_index = random.randint(1, IndexGenerator.give_number_of_elem(cort) - 1)
        new_value = f"{cort_1}[{random_index + 1}]"
        new_elem: Label = Label(Locator(By.XPATH, new_value), "Изменённый локатор new_value")
        return new_elem

    @staticmethod
    def give_number_of_elem(cort):
        """Находим количество элементов из dropdown"""
        elements = BrowserServices.Instance.browser.driver.find_elements(By.CLASS_NAME, cort.value)
        return len(elements)
