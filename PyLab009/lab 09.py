import json
import os
import random
import re
def clean_line(line):
    #                                       Adding a space instead of a newline.
    return line.strip().replace( '-', '' ) + ' '

def add_line():
    ''' a count function.
    summon list char_window, and line number (0). add one to
    the line number count.
    call process char -> appends each char in line to list
    '''
    global char_window, line_number
    line_number += 1
    process_page( ''.join(char_window), line_number )
    char_window.clear()

def process_char(char):
    """window function. Summon the list char_window
    append every char (128) , make a new line"""
    global char_window
    char_window.append(char)
    if len(char_window) == LINE:
        add_line()





def process_page(line, line_num):
    """ access key (line number) is the sting contained in the line
    if the length of window is equivalent to the page(64 lines). call add page"""
    global line_window, pages, page_number
    line_window[line_num] = line
    if len(line_window) == PAGE:
        add_page()


def add_page():
    ''' when add_page is called add 1 to the count of add page. Access
    pages dictionary's key(page number, which is the current count).
    the key will have the value is a copy of {line window}.
    clean the line window list. line_number
    is reassigned to zero'''
    global line_number, line_window, pages, page_number
    page_number += 1
    pages[page_number] = dict(line_window)
    line_window.clear()
    line_number = 0

def read_book(file_path):
    global char_window
    with open(file_path, 'r', encoding='utf-8-sig') as fp:
        for line in fp:
            line = clean_line(line)
            if line.strip():
                for c in line:
                    process_char(c)
    if len(char_window) > 0:
        add_line()
    if len(line_window) > 0:
        add_page()

def process_books(*books):
    for book in books:
        read_book( book )

def generate_code_book():
    global pages
    code_book = {}
    for page, lines in pages.items():
        for num, line in lines.items():
            for pos, char in enumerate(line):
                code_book.setdefault(char, []).append(f'{page}-{num}-{pos}')
    return code_book


def save(file_path, book):
    with open(file_path, 'w') as fp:
        # json.dump(book, fp, indent=4)
        json.dump(book, fp)


def load(file_path, *key_books):
    if os.path.exists(file_path):
        with open(file_path, 'r') as fp, open(file_path.replace('.json', "_r.json"),'r') as fp2:
            return json.load(fp2), json.load(fp),
    else:
        process_books(*key_books)
        save(file_path.replace('.json', "_r.json"), pages)
        code_book = generate_code_book()
        save(file_path, code_book)
        return pages, code_book


def encrypt(code_book, message):
    cipher_text = []
    for char in message:
        index = random.randint(0, len(code_book[char]) - 1)
        cipher_text.append(code_book[char].pop(index))
    return '-'.join(cipher_text)

def decrypt(rev_code_book, ciphertext):
    plaintext = []
    for cc in re.findall(r'\d+-\d+-\d+', ciphertext):
        page, line, char = cc.split('-')
        plaintext.append(
            rev_code_book[page][line][int(char)])
    return ''.join(plaintext)


HOW_MANY_BOOK = 3
LINE = 128 #length of characters in a line
PAGE = 64
pages = {}
page_number = 0
line_window = {}
line_number = 0
char_window = []

process_books('./books/oz.txt')
#print(json.dumps(pages,indent=4))
p,cb =load('./code books/book1.json', './books/oz.txt')
cipher_text = encrypt(cb, 'I am')
print(decrypt(p, cipher_text))