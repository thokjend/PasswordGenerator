import random

def save_password(password):
    f = open("passwords.txt", "a")
    f.write(password + "\n")
    f.close()

def set_length():
    length = int(input("Enter the length of the password: "))
    return length

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

def main():
    length = 10
    use_lowercase = True
    use_uppercase = True
    use_numbers = True
    use_special_chars = True
    counter = 0

    while True:
        print("Password Generator")
        print("---------------------------------------------")
        print(f"1. Set length of password       (Currently: {str(length).ljust(5)})")
        print(f"2. Edit lowercase letters       (Currently: {str(use_lowercase).ljust(5)})")
        print(f"3. Edit uppercase letters       (Currently: {str(use_uppercase).ljust(5)})")
        print(f"4. Edit numbers                 (Currently: {str(use_numbers).ljust(5)})")
        print(f"5. Edit special characters      (Currently: {str(use_special_chars).ljust(5)})")
        print("6. Generate password")
        print("7. Exit")
        print("---------------------------------------------")
        choice = input("Enter your choice (1-7): ")


        if choice == "1":
            length = set_length()
        elif choice == "2":
            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        elif choice == "3":
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        elif choice == "4":
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        elif choice == "5":
            use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        elif choice == "6":
            if counter < 3:
                password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special_chars)
                save_password(password)
                print(f"Your password: {password}")
                counter += 1
            else:
                print("Cannot generate more passwords due to security reasons")
                break
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")    

main()