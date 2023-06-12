# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order
# of the elements may be changed. Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums. More formally, if there are k
# elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements. Return k after placing the final result in the first k slots of
# nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
# extra memory.

# class Solution:
#     def remove_element(self, List, val):
#         k = 0
#         for i in range(len(List)):
#             if List[i] != val:
#                 List[k] = List[i]
#                 k += 1
#         return k
#


class Solution:
    def remove_element(self, lst, num):
        i = 0
        for k in range(0, lst-1):
            if lst[k] != num:
                lst[i] = lst[k]
                i += 1
        return