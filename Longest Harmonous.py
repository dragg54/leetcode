def findHS(nums):
    counter = 0
    res = 0
    i, j = 0, 1
    sortedNums = sorted(nums)
    while j < len(nums):
        diff = sortedNums[j] - sortedNums[i]
        if diff == 1:
            counter += 1
            res = max(res, j - i + 1)
        if diff <= 1:
            counter += 1
            j += 1
        else:
            i += 1
            j = i + 1
            counter = 0
    return res

print(findHS([1,2,2,1]))


