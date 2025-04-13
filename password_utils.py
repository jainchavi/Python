import re

def is_valid_password(password):
    """Validates password strength using a regex limited to numbers and letters only."""
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,}$"
    return re.match(pattern, password) is not None

def encrypt_password(password):
    """Simple encryption: reverses the password string."""
    return password[::-1]

def decrypt_password(encrypted_password):
    """Simple decryption: reverses the encrypted password back."""
    return encrypted_password[::-1]





