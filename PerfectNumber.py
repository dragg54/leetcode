import math


def perfectNumber(num):
    x = int(math.sqrt(num))
    y = int(num/x)
    while x > 0 and y > 0:
        if x * y == num:
            return True
    x += 1
    y
    return False

print(math.sqrt(35))