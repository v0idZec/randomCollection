def decToBin(dec: int) -> int:
    binary: str = ""
    while dec > 0:
        binary += str(dec % 2)
        dec //= 2;
    return int(binary[::-1])