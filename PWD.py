import random
import string

print("=== Random Password Generator ===")

# User input
length = int(input("Enter password length: "))

use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Build character pool
characters = ""

if use_letters:
    characters += string.ascii_letters

if use_numbers:
    characters += string.digits

if use_symbols:
    characters += string.punctuation

# Validation
if not characters:
    print("Error: Select at least one character type!")
    exit()

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)