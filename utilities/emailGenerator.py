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
