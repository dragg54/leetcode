class Solution:
    def find_length(self, word):
        arr = word.split(" ")
        arr_length = len(arr)
        for i in range(len(arr)-1, -1, -1):
            if len(arr[i]) > 0:
                return len(arr[i])


solution = Solution()
print(solution.find_length(" fly me to the moon "))
