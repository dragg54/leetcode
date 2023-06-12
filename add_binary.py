class Solution:
    def addBinary(self, a, b):
        max_len = max(len(a), len(b))
        carry = 0
        res = ""
        _a = a.zfill(max_len)
        _b = b.zfill(max_len)
        digit_a: int = _a[::-1]
        digit_b: int = _b[::-1]
        for i in range(max_len):
            total: int = int(digit_a[i]) + int(digit_b[i]) + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        if carry:
            res = "1" + res
        return res


solution = Solution()
print(solution.addBinary('1101', '110'))

