import random
import string

# Define a function to generate a password
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Run the function to generate a password of length 12
password = generate_password(12)

# Output the generated password
print(password)
