def findLIS(nums):
    counter = 0
    res = 0
    i, j = 0, 1
    while j < len(nums):
        diff = nums[j] - nums[i]
        if diff > 0:
            counter += 1
            res += max(res, counter)
        else:
            counter = 0
        i += 1
        j += 1
    return res
