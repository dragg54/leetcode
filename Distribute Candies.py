def distributeCandies(candyType) -> int:
    nums = set()
    size = len(candyType)
    for i in candyType:
        nums.add(i)
    return min(int(size / 2), len(nums))


print(distributeCandies([1, 2, 2, 3, 3, 4, 5, 5, 6]))
