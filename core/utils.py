import random
import string

def generate_random_passwords(self, num_passwords=5, password_length=8):
        passwords = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(password_length)) for _ in range(num_passwords)]
        return ','.join(passwords)

# def generate_random_password(length=8):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for _ in range(length))
