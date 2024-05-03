import string
import random

def generate_short_url():

    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))  # Adjust the length as needed # Adjust the length as needed
    return short_url

