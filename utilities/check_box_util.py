import random
from py_selenium_auto.browsers.browser_services import BrowserServices
from selenium.webdriver.common.by import By


class CheckBoxUtil:
    @staticmethod
    def give_number_of_elem(cort):
        """Находим количество элементов из dropdown"""
        elements = BrowserServices.Instance.browser.driver.find_elements(By.CLASS_NAME, cort)
        return elements

    @staticmethod
    def get_unique_values_from_checkbox_labels(class_name_of_elements, class_name_of_element, unique_label):
        """Получаем уникальные значения из атрибута 'for' элементов checkbox__label"""
        elements = CheckBoxUtil.give_number_of_elem(class_name_of_elements)
        # Список для хранения уникальных значений 'for'
        unique_values = []
        # Итерируемся по каждому элементу
        for element in elements:
            # Находим вложенный элемент с классом 'checkbox__label'
            label = element.find_element(By.CLASS_NAME, class_name_of_element)

            # Проверяем, что элемент найден
            if label:
                # Извлекаем значение атрибута 'for' и добавляем его в список
                for_attribute = label.get_attribute(unique_label)
                unique_values.append(for_attribute)
                print(unique_values)
        return unique_values

    @staticmethod
    def click_checkbox_by_for_value(for_value):
        """Кликает на чекбокс по значению атрибута 'for'"""
        checkbox = BrowserServices.Instance.browser.driver.find_element(By.XPATH, f'//*[@for="{for_value}"]')
        if checkbox:
            checkbox.click()

    @staticmethod
    def click_random_checkboxes(values, excluded_values=None, num_checkboxes=3):
        """Рандомно кликает на чекбоксы"""
        if excluded_values is None:
            excluded_values = []

        # Создаем копию списка значений
        available_values = list(values)

        # Удаляем значения, которые нужно исключить
        available_values = [value for value in available_values if value not in excluded_values]

        # Рандомно выбираем и кликаем на чекбоксы
        for _ in range(num_checkboxes):
            random_value = random.choice(available_values)
            CheckBoxUtil.click_checkbox_by_for_value(random_value)
            available_values.remove(random_value)
