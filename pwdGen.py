import secrets
import string
import random

# TODO: improve

def genPass(length = 42, letters = True, digits = True, extras = True) -> str:
    assert length >= 16
    assert sum([letters, digits, extras]) >= 2

    chars = list((string.ascii_letters if letters else '') + (string.digits if digits else '') + (string.punctuation if extras else ''))

    pwd = ""
    for _ in range(length):
        random.shuffle(chars)
        pwd += secrets.choice(chars)

    return pwd