#lefchiper/core/lefchaos.py
import random

def chaos_encrypt(text: str, key: str) -> str:
    random.seed(key)
    indices = list(range(len(text)))
    random.shuffle(indices)

    shuffled = [''] * len(text)
    for i, idx in enumerate(indices):
        shuffled[idx] = text[i]

    return ''.join(shuffled)

def chaos_decrypt(cipher: str, key: str) -> str:
    random.seed(key)
    indices = list(range(len(cipher)))
    random.shuffle(indices)

    unshuffled = [''] * len(cipher)
    for i, idx in enumerate(indices):
        unshuffled[i] = cipher[idx]

    return ''.join(unshuffled)
