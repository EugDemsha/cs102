import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:

    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    for a in plaintext:
        if a.isalpha():
            if a.istitle():
                a = chr(ord(a) + shift)
                if ord(a) > ord("Z"):
                    a = chr(ord(a) - 26)
            else:
                a = chr(ord(a) + shift)
                if ord(a) > ord("z"):
                    a = chr(ord(a) - 26)
        ciphertext += a
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    for a in ciphertext:
        if a.isalpha():
            if a.istitle():
                a = chr(ord(a) - shift)
                if ord(a) < ord("A"):
                    a = chr(ord(a) + 26)
            else:
                a = chr(ord(a) - shift)
                if ord(a) < ord("a"):
                    a = chr(ord(a) + 26)
        plaintext += a
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
