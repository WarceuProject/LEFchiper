#lefchiper/core/lefkey.py
import secrets
import string

def generate_key(length=32, charset="ascii"):
    if charset == "ascii":
        chars = string.ascii_letters + string.digits + string.punctuation
    elif charset == "hex":
        chars = string.hexdigits
    elif charset == "digits":
        chars = string.digits
    elif charset == "letters":
        chars = string.ascii_letters
    else:
        raise ValueError("Charset tidak dikenal.")

    return ''.join(secrets.choice(chars) for _ in range(length))
