from backend.core.security import (
    create_access_token,
    decode_access_token,
    get_password_hash,
    verify_password,
)


def test_password_hashing():
    password = "CyberPulse123!"
    hashed = get_password_hash(password)

    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("wrongpassword", hashed) is False


def test_token_generation_and_verification():
    token = create_access_token("tester")
    data = decode_access_token(token)

    assert data
    assert data.get("sub") == "tester"


def test_invalid_token():
    invalid_token = "invalid.token.structure"
    data = decode_access_token(invalid_token)

    assert data == {}