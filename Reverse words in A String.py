def reverseWords(str):
    words = str.split(' ')
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)

print(reverseWords("I want to go mayor's house"))
