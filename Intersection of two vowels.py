def intersection(nums1, nums2):
    result = []
    for i in nums1:
        if i not in result and i in nums2:
            result.append(i)
    return result
            