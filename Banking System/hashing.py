import hashlib  # Importing the hashlib module to use hashing functions for security

def hash_pin(self, pin, salt):
        # Method in hashing the PIN using SHA-256 and salt
        return hashlib.sha256((pin + salt).encode()).hexdigest()

