def getThirdMax(arr):
    first_max = None
    second_max = None
    third_max = None
    if len(arr) == 1:
        return arr[-1]
    nums = list(set(arr))
    for i in range(len(nums)):
        if first_max and nums[i] > first_max:
            tmp_1 = first_max
            tmp_2 = second_max
            first_max = nums[i]
            second_max = tmp_1
            third_max = tmp_2
        elif not first_max and not second_max:
            first_max = nums[i]
        elif second_max and nums[i] > second_max:
            tmp_1 = second_max
            second_max = nums[i]
            third_max = tmp_1
        elif not second_max and nums[i] < first_max:
            second_max = nums[i]
        elif third_max and nums[i] > third_max:
            third_max = nums[i]
        elif not third_max and nums[i] < second_max:
            third_max = nums[i]
    if third_max:
        return third_max
    else:
        return first_max

print(getThirdMax([3,3,4,3,4,3,0,3,3]))

