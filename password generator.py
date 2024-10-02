import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    # Define character sets based on user preferences
    lower_case = string.ascii_lowercase if use_lower else ''
    upper_case = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine selected character sets
    all_characters = lower_case + upper_case + digits + symbols

    # Ensure at least one character from each selected category is included
    password_chars = []
    if use_lower:
        password_chars.append(random.choice(lower_case))
    if use_upper:
        password_chars.append(random.choice(upper_case))
    if use_digits:
        password_chars.append(random.choice(digits))
    if use_symbols:
        password_chars.append(random.choice(symbols))

    # Fill the rest of the password length with random choices from the combined character set
    remaining_length = length - len(password_chars)
    if remaining_length > 0:
        password_chars += random.choices(all_characters, k=remaining_length)

    # Shuffle the resulting characters to ensure randomness
    random.shuffle(password_chars)

    # Join the list into a string
    password = "".join(password_chars)
    return password

# Set parameters for password generation
password_length = 12  # You can adjust this value
password = generate_password(length=password_length)
print("Your secure password is:", password)
