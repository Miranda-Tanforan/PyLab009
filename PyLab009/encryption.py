

def letter_to_index(letter, alphabet):
    for i, c in enumerate(alphabet):
        if letter == c:
            return i
    return  None

def index_to_letter(index:int ,alphabet:str ):
    if 0 <= index <= alphabet_len:
        return alphabet[index]
    return None

def vigenere_index(key_letter, plaintext_letter, alphabet):
    ci = (letter_to_index(key_letter,alphabet) + letter_to_index(plaintext_letter,alphabet)) % alphabet_len
    return index_to_letter(ci,alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    for i, pt in enumerate(plaintext):
        cipher_text.append(vigenere_index(key[i% len(key)], pt, alphabet))
    return ''.join(cipher_text)

def anti_vignere_index(key_letter, cipher_letter, alphabet):
    pi = (letter_to_index(cipher_letter, alphabet) - letter_to_index(key_letter, alphabet)) % alphabet_len
    return index_to_letter(pi, alphabet)

def decrypt_vigenere(key, ciphertext, alphabet):
    plaintext = []
    for i,ct in enumerate(ciphertext):
        plaintext.append(anti_vignere_index(key[i % len(key)], ct, alphabet))
    return ''.join(plaintext)
