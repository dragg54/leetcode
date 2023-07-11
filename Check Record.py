def checkRecord(self, s: str) -> bool:
    countA = 0
    for i in range(len(list(s))):
        if i + 3 <= len(s) and s[i] == "L" and s[i + 1] == "L" and s[i + 2] == "L":
            return False
        if s[i] == "A":
            countA += 1
    if countA >= 2:
        return False
    return True