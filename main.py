#3
import random

class PasswordGenerator:
    def __init__(self, length, characters):
        self.length = length
        self.characters = characters

    def generate_password(self):
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password

length = 8
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/.,:"][{}=+-_'

password_gen = PasswordGenerator(length, characters)

print(password_gen.generate_password())
