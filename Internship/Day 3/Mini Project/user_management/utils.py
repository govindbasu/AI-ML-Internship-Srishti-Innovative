import hashlib

def validate_password(password):
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters")
    return True

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()