def longest_prefix(arr):
    prefix = []
    first_word = arr[0]
    for i in range(0, len(get_shortest_word(arr)[0])):
        for j in range(1, len(arr)):
            if first_word[i] == arr[j][i]:
                continue
            if first_word[i] != arr[j][i]:
                return ''.join(prefix)
        prefix.append(first_word[i])
    return ''.join(prefix)


def get_shortest_word(arr):
    word = [arr[0]]
    for i in range(1, len(arr)):
        if len(arr[i]) < len(word[0]):
            word[0] = arr[i]
    return word


print(longest_prefix(["", ""]))
