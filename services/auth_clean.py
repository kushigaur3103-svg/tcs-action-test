"""
Authentication service module providing secure password hashing and verification.
Realistic safe business logic with no security vulnerabilities.
"""

import re
import hmac
import hashlib


def validate_username(username: str) -> bool:
    """Validate username against strict alphanumeric pattern."""
    if not username or not isinstance(username, str):
        return False
    return bool(re.match(r"^[a-zA-Z0-9_-]{3,32}$", username))


def hash_password(password: str, salt: bytes) -> bytes:
    """Generate secure password hash using PBKDF2 HMAC SHA-256."""
    if not password or len(password) < 8:
        raise ValueError("Password must be at least 8 characters.")
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)


def verify_password(stored_hash: bytes, provided_password: str, salt: bytes) -> bool:
    """Constant-time verification of password hash against stored record."""
    computed_hash = hash_password(provided_password, salt)
    return hmac.compare_digest(stored_hash, computed_hash)
