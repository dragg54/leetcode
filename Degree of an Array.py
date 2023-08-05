def findShortestSubArray( nums):
    count = {}
    firstVisit = {}
    degree = 0
    minVal = 0
    for i in range(len(nums)):
        if nums[i] not in firstVisit:
            firstVisit[nums[i]] = i
        count[nums[i]] = 1 + count.get(nums[i], 0)
        if count[nums[i]] > degree:
            degree = count[nums[i]]
            minVal = i - firstVisit[nums[i]] + 1
        elif count[nums[i]] == degree:
            minVal = min(minVal, i - firstVisit[nums[i]] + 1)
    return minVal