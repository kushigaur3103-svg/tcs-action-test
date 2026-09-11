def calculate_security_hash(payload: str) -> str:
    """A clean, secure utility function with no vulnerabilities."""
    import hashlib
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    result = calculate_security_hash("clean test input")
    print(f"Hash: {result}")
