def arrangeCoins( n: int) -> int:
    res = 0
    checker = 0
    while checker < n:
        res += 1
        checker += 1
        n -= checker
    return res

print(arrangeCoins(5))