import random
import string


class GenerateRandomText:

    @staticmethod
    def generate_random_text(length=10):
        """Генерирует случайную строку указанной длины."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))


