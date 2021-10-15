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
    # PUT YOUR CODE HERE
    if len(keyword) < len(plaintext):
        for i in keyword:
            if len(keyword) < len(plaintext):
                keyword += i
        return encrypt_vigenere(plaintext, keyword)
    else:
        for a in range(len(plaintext)):
            b = plaintext[a]
            c = keyword[a]
            if c.istitle():
                shift = ord(c) - ord("A")
            else:
                shift = ord(c) - ord("a")
            if b.isalpha():
                if b.istitle():
                    b = chr(ord(b) + shift)
                    if ord(b) > ord("Z"):
                        b = chr(ord(b) - 26)
                else:
                    b = chr(ord(b) + shift)
                    if ord(b) > ord("z"):
                        b = chr(ord(b) - 26)
            ciphertext += b

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
    # PUT YOUR CODE HERE
    if len(keyword) < len(ciphertext):
        for i in keyword:
            if len(keyword) < len(ciphertext):
                keyword += i
        return decrypt_vigenere(ciphertext, keyword)
    else:
        for a in range(len(ciphertext)):
            b = ciphertext[a]
            c = keyword[a]
            if c.istitle():
                shift = ord(c) - ord("A")
            else:
                shift = ord(c) - ord("a")
            if b.isalpha():
                if b.istitle():
                    b = chr(ord(b) - shift)
                    if ord(b) < ord("A"):
                        b = chr(ord(b) + 26)
                else:
                    b = chr(ord(b) - shift)
                    if ord(b) < ord("a"):
                        b = chr(ord(b) + 26)
            plaintext += b

    return plaintext
