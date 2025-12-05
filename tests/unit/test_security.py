from backend.security.auth import verify_token, generate_token
from backend.security.hashing import hash_password, verify_password

def test_password_hashing():
    pwd = "CyberPulse123!"
    hashed = hash_password(pwd)

    assert hashed != pwd
    assert verify_password(pwd, hashed) is True
    assert verify_password("wrongpassword", hashed) is False

def test_token_generation_and_verification():
    token = generate_token({"user": "tester"})
    data = verify_token(token)

    assert data is not None
    assert data.get("user") == "tester"

def test_invalid_token():
    invalid = "invalid.token.structure"
    data = verify_token(invalid)

    assert data is None
