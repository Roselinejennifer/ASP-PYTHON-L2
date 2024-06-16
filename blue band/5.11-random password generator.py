import random
import string
password_length = int(input("Enter the desired password length:"))
include_numbers = input("Include numbers?(yes/no):").lower() =='yes'
include_symbols = input("Include symbols?(yes/no):").lower() =='yes'
characters = string.ascii_letters
if include_numbers:
    characters += string.digits
if include_symbols:
    characters += string.punctuation
generated_password = ''.join(random.choice(characters) for _ in range(password_length))
print("charcters:",characters)
print("characters password:",generated_password)


