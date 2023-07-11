def nextGreatestElement(nums1, nums2):
    i,j = 0,0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j] :
            while j < len(nums2):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    i += 1
                    j = 0
                    break
                elif j == len(nums2) - 1:
                    res.append(-1)
                    i += 1
                    j = 0
                    break
                else:
                    j += 1
        else:
            j += 1
    return res


print(nextGreatestElement([4, 1, 2], [1, 3, 4, 2]))