# import string
# import secrets
import random


def generate_short_id(size=9, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(chars) for _ in range(size))


# def generate_random_unique_long_characters(length):
#     characters = string.ascii_letters + string.digits + string.punctuation  # Include letters, digits, and punctuation
#     unique_chars = set()

#     while len(unique_chars) < length:
#         char = secrets.choice(characters)
#         unique_chars.add(char)

#     return ''.join(unique_chars)

# Generate 20 random unique long characters
# random_chars = generate_random_unique_long_characters(20)
# print(random_chars)