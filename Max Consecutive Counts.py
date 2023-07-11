from ast import List
def findMaxConsecutiveOnes(nums) -> int:
    i, j = 0, 0
    count = 0
    maxCount = 0
    while j < len(nums):
        if nums[i]==1 and nums[j] == 1:
            count += 1
            j += 1
        else:
            i = j+1
            j = i
            maxCount = max(count, maxCount)
            count = 0
    return max(maxCount, count)

print(findMaxConsecutiveOnes([1,1,1,1,0,1,1,1,1,1]))