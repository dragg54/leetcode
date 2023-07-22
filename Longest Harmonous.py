# def findLHS(nums) -> int:
#     left = 0
#     right = 1
#     result = 0
#     nums = sorted(nums)
#     while right < len(nums):
#         diff = nums[right] - nums[left]
#         if diff == 1:
#             result = max(result, right - left + 1)
#         if diff <= 1:
#             right += 1
#         else:
#             left += 1
#     return result
#
# print(findLHS([1,3,2,2,5,2,3,7]))

def LHS(nums):
    maxRes = 0
    sortedNums = sorted(nums)
    i, j = 0, 1
    while i < len(nums):
        diff = nums[i] - nums[j]
            if diff > 1:
                i += j
                j += 1
            if diff <= 1:
                maxRes = max(maxRes, j - 1 + 1)
                j += 1


