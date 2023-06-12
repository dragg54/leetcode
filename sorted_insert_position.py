# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums, val):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == val:
                return mid
            if nums[mid] > val:
                r = mid - 1
            else:
                l = mid + 1
        return l

solution = Solution()
print(solution.searchInsert([1, 3, 4, 5, 6], 2))
