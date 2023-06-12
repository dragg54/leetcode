# class Solution:
#     def remove_duplicates(self, List):
#         left = 1
#         for right in range(1, len(List)):
#             if List[right] != List[right - 1]:
#                 List[left] = List[right]
#                 left += 1
#         return left
#
