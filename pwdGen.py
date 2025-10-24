from secrets import choice
from random import shuffle
from string import ascii_letters, digits, punctuation

# TODO: improve

def genPass(length = 42, letters = True, numbers = True, extras = True) -> str:
    assert length >= 16
    assert sum([letters, numbers, extras]) >= 2

    chars = list((ascii_letters if letters else '') + (digits if numbers else '') + (punctuation if extras else ''))

    pwd = ""
    for _ in range(length):
        shuffle(chars)
        pwd += choice(chars)

    return pwd
