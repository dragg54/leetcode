def findTheDifference(s: str, t: str) -> str:
    mapX = {}
    mapY = {}
    for i in s:
        mapX[i] = 1 + mapX.get(i, 0)
    for j in t:
        mapY[j] = 1 + mapY.get(j, 0)
    for k in t:
        if k not in mapX or mapY[k] > mapX[k]:
            return k