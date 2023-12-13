import random
from utilities.generateRandomText import GenerateRandomText


class EmailGenerator:

    @staticmethod
    def generate_email(length=8):
        """Генерирует случайный email."""
        username = GenerateRandomText.generate_random_text(length)
        return username

    @staticmethod
    def generate_domain(domain_list=None):
        """Выбирает случайный domain из списка."""
        domain = domain_list or ['mail', 'yandex', 'gmail', 'outlook', 'yahoo', 'aol', 'icloud', 'protonmail', 'zoho', 'inbox',
               'mailfence', 'tutanota', 'fastmail', 'gmx', 'aol', 'mailchimp', 'hushmail', 'rackspace', 'runbox', 'yopmail']
        return random.choice(domain)

class ComboBoxIndexGenerator:
    def __init__(self, dropdown_locator):
        self.dropdown_locator = dropdown_locator
        self.dropdown_items_locator = f"{dropdown_locator}/*[@class='dropdown__list-item']"
        self.selected_index = None

    def generate_random_index(self):
        dropdown_items = self.get_dropdown_items()
        self.selected_index = random.randint(0, len(dropdown_items) - 1)
        return self.selected_index

    def get_dropdown_items(self):
        return self.driver.find_elements_by_xpath(self.dropdown_items_locator)

    def get_selected_index(self):
        return self.selected_index

# Пример использования
# dropdown_locator = "//*[@class='dropdown__list']"
# generator = ComboBoxIndexGenerator(dropdown_locator)
# random_index = generator.generate_random_index()
# print(f"Выбранный случайный индекс: {random_index}")

# Теперь вы можете использовать random_index в вашем методе select_dot_org
# Например:
# __DropdownCmbXpath: str = f"{dropdown_locator}/div[@class='dropdown__list-item'][{random_index + 1}]"
# self.dropdown_dot_com = ComboBox(Locator(By.XPATH, self.__DropdownCmbXpath), "dropdown_dot_com")
# self.dropdown_opener.click()
# self.dropdown_dot_com.click()