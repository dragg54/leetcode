def reverseVowels(str):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels_in_str = []
    result = []
    for c in str:
        if c.lower() in vowels:
            vowels_in_str.append(c)
            result.append(None)
        else:
            result.append(c)
    for i, item in enumerate(result):
        if item is None:
            result[i] = vowels_in_str.pop()
    return "".join(result)

print(reverseVowels(("hello")))