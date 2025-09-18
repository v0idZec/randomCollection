def binToDec(binary: int) -> int:
    c: int = 1;
    decimal: int = 0
    for n in reversed(str(binary)):
        if n == '1':
            decimal += c
        c *= 2
    return decimal