import random
import string

def generate_password():
    length = int(input("Enter the desired password length: "))
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    print("Generated Password:", password)

generate_password()
