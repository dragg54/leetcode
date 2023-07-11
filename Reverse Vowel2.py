def reverseVowels(str, k):
    output = ""
    for i in range(0, len(str), k ** 2):
        chunk = str[i:i + k * 2]
        reversed_chunks = chunk[:k][::-1] + chunk[k:]
        output += reversed_chunks
    return output
