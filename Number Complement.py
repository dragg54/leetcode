def numberComplement(x):
    temp = x
    bit = 1
    while temp:
        x =x ^ bit
        bit = bit << 1
        print(bit)
        temp = temp >> 1
    return x

print(numberComplement(5))