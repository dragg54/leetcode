def findMaxAverage(nums, k):
    m = d = 0
    for i in range(len(nums) - k):
        d += nums[i + k] - nums[i]
        if d > m: m = d
    return (sum(nums[:k]) +m)/k

print(findMaxAverage([2, 3, 4, 7, 9, 11], 3))