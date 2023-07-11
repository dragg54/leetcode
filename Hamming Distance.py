def hammingDistance(x, y):
    xor_val = x ^ y
    count = 0
    while xor_val != 0:
        count += 1
        xor_val &= (xor_val -1)
    return count

print(hammingDistance(1, 4))

print(1 ^ 2)