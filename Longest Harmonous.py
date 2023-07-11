def findLHS(self, nums) -> int:
    left = 0
    right = 1
    result = 0
    nums = sorted(nums)
    while right < len(nums):
        diff = nums[right] - nums[left]
        if diff == 1:
            result = max(result, right - left + 1)
        if diff <= 1:
            right += 1
        else:
            left += 1
    return result