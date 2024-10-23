import random

print("Password Generator")
length = int(input("Enter the length of the password: "))

def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special_chars):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    character_pool = ""
    
    if use_lowercase:
        character_pool += lowercase_letters
    if use_uppercase:
        character_pool += uppercase_letters
    if use_numbers:
        character_pool += numbers
    if use_special_chars:
        character_pool += special_characters

    if character_pool:
        password = ''.join(random.choices(character_pool, k=length))
    else:
        password = ""

    return password
   
password = generate_password(length, True, True, True, True)
print(f"Your password: {password}")