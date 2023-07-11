def findNumberDisappearedFromArray(nums):
    for i in nums:
        n = abs(i) - 1
        nums[n] = -1 * abs(nums[n])
    res = []
    for i,n in enumerate(nums):
        if n > 0:
            res.append(i + 1)
    return res

print(findNumberDisappearedFromArray([1, 3, 3, 4, 5]))
