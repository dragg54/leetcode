def isPlaindrome(str):
    newStr = ""
    for i in str:
        if i.isalnum():
            newStr += i.lower()
    return newStr == newStr[::-1]