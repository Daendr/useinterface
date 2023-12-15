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
