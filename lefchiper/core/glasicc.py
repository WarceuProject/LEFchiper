def glasicc_encrypt(text):
    hasil = ''
    for char in text:
        lower = char.lower()
        if lower in 'aiueo':
            hasil += f'{char}g{lower}'
        else:
            hasil += char
    return hasil

def glasicc_decrypt(text):
    hasil = ''
    i = 0
    while i < len(text):
        char = text[i]
        if i + 2 < len(text) and text[i+1] == 'g' and text[i+2].lower() == text[i].lower():
            hasil += char
            i += 3
        else:
            hasil += char
            i += 1
    return hasil
