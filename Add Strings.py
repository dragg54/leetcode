def addStrings(s, t):
    max_len = max(len(s), len(t))
    revS = s[::-1]
    revT = t[::-1]

    res = ""
    carry = 0
    for i in range(max_len):
        while
        if not s[i]:
            s[i] = 0
        if not t[i]:
            t[i] = 0
        total = int(revS[i]) + int(revT[i]) + carry
        char = str(total % 10)
        res = res + char
        carry = total // 10
    if carry > 1:
        res.append(carry)
    return res[::-1]


print(addStrings("123", "15"))
