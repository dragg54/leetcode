def convertToBase7(num):
    tmp = num
    res = ""
    if num < 0:
        num = num * -1
    while num > 0:
        rem = num % 7
        res += str(rem)
        num = num // 7
    if tmp < 0:
        return "-"+ res[::-1]
    else:
        return res[::-1]
print(convertToBase7(7))