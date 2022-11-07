def linealSearch(values, target):
    i = 0
    while i < values.__len__():
        if values[i] == target:
            return i

        if values[i] > target:
            return -1
        i += 1

    return -1
