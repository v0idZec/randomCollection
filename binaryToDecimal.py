def binToDec(binary) -> int:
    decimal = 0
    c = 1;

    for n in reversed(str(binary)):
        if n == '1':
            decimal += c
        c *= 2
        
    return decimal