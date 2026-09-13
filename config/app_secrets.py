"""
Application secrets and configuration fixture.
"""

# 1. Known deterministic secret fixture (AWS Access Key ID pattern)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"

# 2. Placeholder environment string (must NOT be classified merely due to SECRET naming)
API_SECRET_KEY = "dummy_env_placeholder"

# 3. Innocuous base64-looking encoded string (1x1 transparent PNG)
DEFAULT_AVATAR_B64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
