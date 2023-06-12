def dupl(list):
    hashset = set()
    for n in list:
        if n in hashset:
            return True
        hashset.add(n)
    return False
