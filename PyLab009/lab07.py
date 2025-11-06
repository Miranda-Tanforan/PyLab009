


def print_row(a:int):
    row = []
    for c in range(alphabet_len):
        row.append(alphabet[(c + a) % alphabet_len])
        #print (f' {alphabet[(c + a) % alphabet_len]} |', end='')
    #print()
    return row
def print_header():
    header = [' ']
    #print(f' ||', end ='')
    for a in alphabet:
        header.append(a)
        #print(f' {a} |', end = '')
    #print()
    #suffix = "---|" * (alphabet_len)
    #print(f'  |{suffix}', end ='')
    return header
def vigenere_sq():
    sq = []
    header = print_header()
    sq.append(header)
    for a in range(alphabet_len):
        row = print_row(a)
        row.insert(0,alphabet[a])
        sq.append(row)
    return sq

def pretty_print(vsq:list):
    for i,row in enumerate(vsq):
        print(' | '.join(row))
        #if i == 0:
        #    suffix = "---|" * (alphabet_len+1)
        #    print(f'  |{suffix}', end ='')



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

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
alphabet_len = len(alphabet)

key = 'MONKEY'
plaintext = 'LIGHTHOUSES ARE COOL'
ciphertext = 'XWTRXE HEOWXMERJGL Z'
#et = encrypt_vigenere(key, plaintext, alphabet)
#print(et)

#pt =decrypt_vigenere(key,et,alphabet)

#print(pt)


choice = 0
et_list = []
pt_list = []

print('1. Encrypt a word to list')
print('2. Decrypt a word in list')
print('3. Clear list')
print('4. Exit')


while choice != 4:
    choice = int(input('Enter choice[1,2,3,4]: '))
    if not (1<= choice <= 4):
        continue
    if choice == 1:
        message = input('Enter message: ').upper()
        et_list.append(encrypt_vigenere(key, message, alphabet))
        print(f'Encrypted words: {et_list}')
    if choice == 2:
        for ct in et_list:
            print(decrypt_vigenere(key, ct, alphabet))
    if choice == 3:
        et_list.clear()
        print('List has been cleared')
        #(decrypt_vigenere(key, message, alphabet))
    if choice == 4:
        print("thanks for playing")
        break