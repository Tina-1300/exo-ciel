import string
import secrets

def generate_password(length=8, use_uppercase=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_uppercase:chars += string.ascii_uppercase
    if use_digits:chars += string.digits
    if use_special:chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    while True:
        password = ''.join(secrets.choice(chars) for _ in range(length))
        
        # Vérifier la complexité
        if (any(c.islower() for c in password) and
            (not use_uppercase or any(c.isupper() for c in password)) and
            (not use_digits or any(c.isdigit() for c in password)) and
            (not use_special or any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password))):
            return password


print(generate_password())