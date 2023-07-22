def setMismatch(nums):
    res = []
    sortedNums = sorted(nums)
    for i in range(len(sortedNums)):
        nums[sortedNums[i] - 1] = -1 * abs(sortedNums[i])
    for i in range(len(sortedNums)):
        if (i+1) + sortedNums[i] != 0:
            res.append(i + 1)
    return res

print(setMismatch([2, 3, 3, 4, 5, 6]))