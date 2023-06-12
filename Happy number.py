class Solution:
    def isHappy(self, num):
        visited = set()
        while num not in visited:
            visited.add((num))
            num = self.sumOfSquare(num)
            if num == 1:
                return True
        return False

    def sumOfSquare(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output