import random
import string
from utilities.generateRandomText import GenerateRandomText


class PasswordGenerator:

    @staticmethod
    def generate_password(email):
        """Генерирует пароль с учетом указанных требований."""
        password = GenerateRandomText.generate_random_text()

        # Проверка требования: "Ваш пароль должен содержать минимум 1 заглавную букву."
        if not any(char.isupper() for char in password):
            password = password[:1].upper() + password[1:]

        # Проверка требования: "Ваш пароль должен содержать минимум 1 цифру."
        if not any(char.isdigit() for char in password):
            password += random.choice(string.digits)

        # Проверка требования: "Ваш пароль должен содержать минимум 1 букву из вашего email."
        email_letter = next((char.lower() for char in email if char.isalpha()), None)
        if email_letter and email_letter not in password:
            password += email_letter

        # Проверка требования: "Ваш пароль может содержать минимум 1 кириллический символ."
        cyrillic_char = random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        if cyrillic_char not in password:
            password += cyrillic_char

        return password
