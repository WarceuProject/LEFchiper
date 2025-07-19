from lefchiper.core.lefchaos import chaos_encrypt, chaos_decrypt

def test_chaos_encrypt_decrypt():
    text = "Hello Chaos!"
    key = "mysecretkey"
    encrypted = chaos_encrypt(text, key)
    decrypted = chaos_decrypt(encrypted, key)
    assert decrypted == text
