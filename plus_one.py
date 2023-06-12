def plusOne(arr):
    rem = 0
    rev = arr[::-1]
    for i in range(len(arr)):
        if rev[i] == 9:
            rev[i] = 0
            if i == len(arr) - 1:
                rem = 1
        else:
            rev[i] = rev[i] +1
            break
        i += 1
    if rem > 0:
        rev.append(1)
        return rev[::-1]
    else:
        return rev[::-1]

print(plusOne([1, 9, 9]))