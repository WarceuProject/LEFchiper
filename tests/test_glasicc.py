from lefchiper.core.glasicc import caesar_encrypt, caesar_decrypt

def test_encrypt_decrypt():
    text = "Hello World!"
    encrypted = caesar_encrypt(text, shift=5)
    decrypted = caesar_decrypt(encrypted, shift=5)
    assert decrypted == text
