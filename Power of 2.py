def powerOfTwo(n):
    counter = 1
    while counter < n:
        counter *= 2
    return counter == n

print(powerOfTwo(15))