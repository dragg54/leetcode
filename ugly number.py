def isUgly(n: int) -> bool:
    pri_nums = [2, 3, 5]
    res = 0
    for i in range(0, len(pri_nums)):
        if n % pri_nums[i] == 0 and n != 1:
            while n % pri_nums[i] == 0 and n != 1:
                n = n / pri_nums[i]
        i += 1
    if n != 1:
        return False
    return True

print(isUgly(20))