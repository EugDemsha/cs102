def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    count = 0
    while len(plaintext) > len(keyword):
        keyword += keyword[count]
        count += 1
    else:
        for num in range(len(plaintext)):
            symbol_to_code = plaintext[num]
            key_symbol = keyword[num]
            if key_symbol.isupper():
                shift = ord(key_symbol) - ord("A")
            else:
                shift = ord(key_symbol) - ord("a")
            if symbol_to_code.isalpha():
                if symbol_to_code.isupper():
                    symbol_to_code = chr(ord(symbol_to_code) + shift)
                    if ord(symbol_to_code) > ord("Z"):
                        symbol_to_code = chr(ord(symbol_to_code) - 26)
                else:
                    symbol_to_code = chr(ord(symbol_to_code) + shift)
                    if ord(symbol_to_code) > ord("z"):
                        symbol_to_code = chr(ord(symbol_to_code) - 26)
            ciphertext += symbol_to_code

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    count = 0
    while len(ciphertext) > len(keyword):
        keyword += keyword[count]
        count += 1
    else:
        for num in range(len(ciphertext)):
            symbol_to_decode = ciphertext[num]
            key_symbol = keyword[num]
            if key_symbol.isupper():
                shift = ord(key_symbol) - ord("A")
            else:
                shift = ord(key_symbol) - ord("a")
            if symbol_to_decode.isalpha():
                if symbol_to_decode.isupper():
                    symbol_to_decode = chr(ord(symbol_to_decode) - shift)
                    if ord(symbol_to_decode) < ord("A"):
                        symbol_to_decode = chr(ord(symbol_to_decode) + 26)
                else:
                    symbol_to_decode = chr(ord(symbol_to_decode) - shift)
                    if ord(symbol_to_decode) < ord("a"):
                        symbol_to_decode = chr(ord(symbol_to_decode) + 26)
            plaintext += symbol_to_decode

    return plaintext
