import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""
# Define the characters pool based on user preferences
# Lenght is initially setted to 12   
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
        
# Check if no character options were selected
    if not characters:
        return "Error: No character options selected."
        
# Generate the password by randomly choosing characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def Generator():
    print("Welcome to the Password Generator!")

# Get user preferences for password generation
    length = int(input("Enter the desired password length: "))
    
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Generate the password based on user preferences
    password = generate_password(length, uppercase, lowercase, digits, special_chars)

# Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    Generator()
