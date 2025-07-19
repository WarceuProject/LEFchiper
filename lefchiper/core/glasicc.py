# lefchiper/core/glasicc.py

def glasicc_encrypt(text, key=None):
    result = ''
    vowels = 'aiueo'
    for char in text:
        if char in vowels:
            result += char + 'g' + char
        else:
            result += char
    return result

def glasicc_decrypt(text, key=None):
    result = ''
    i = 0
    while i < len(text):
        if text[i] in 'aiueo':
            if i+2 < len(text) and text[i+1] == 'g' and text[i+2] == text[i]:
                result += text[i]
                i += 3
            else:
                result += text[i]
                i += 1
        else:
            result += text[i]
            i += 1
    return result
