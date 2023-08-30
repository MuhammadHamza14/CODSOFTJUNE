import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        return "Error: No character options selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def Generator():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired password length: "))
    
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    
    print("Generated Password:", password)

if __name__ == "__main__":
    Generator()
