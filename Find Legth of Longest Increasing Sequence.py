def findLHS(nums):
    trackerA = 0
    counterA = 1
    i, j = 0, 1
    while i < len(nums) - 1:
        counterB = 1
        diff = nums[j] - nums[i]
        if diff == trackerA:
            counterA += 1
            counterB += 1
        else:
            trackerA = diff
            counterB = 1
            counterA = max(counterA, counterB)
        i += 1
        j += 1
    return counterA