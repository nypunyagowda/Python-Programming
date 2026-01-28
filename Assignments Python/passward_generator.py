import random
import string

# Characters allowed in password
characters = string.ascii_letters + string.digits

# Generate 8-character password
password = ""
for i in range(8):
    password += random.choice(characters)

print("Generated Password:", password)
