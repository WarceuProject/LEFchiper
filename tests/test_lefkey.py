from lefchiper.core.lefkey import generate_key

def test_generate_default_key():
    key = generate_key()
    assert len(key) == 32

def test_generate_custom_length():
    key = generate_key(length=16)
    assert len(key) == 16

def test_generate_hex_key():
    key = generate_key(length=20, charset="hex")
    assert all(c in "0123456789abcdefABCDEF" for c in key)
