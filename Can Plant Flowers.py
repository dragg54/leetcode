def canPlantFlowers(flowerbed, n):
    bed = [0] + flowerbed + [0]
    for i in range(1, len(bed) - 1):
        if bed[i - 1] == 0 and bed[i + 1] == 0 and bed[i] == 0:
            bed[i] = 1
            n -= 1
    return n <= 0