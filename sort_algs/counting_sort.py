def counting_sort(values, max_value):
    counts = [0] * (max_value + 1)
    for value in values:
        counts[value] += 1

    index = 0
    for i in range(max_value + 1):
        for j in range(counts[i]):
            values[index] = i
            index += 1


data = [1, 2, 2, 1, 0, 2, 2, 1, 0, 2]
counting_sort(data, 2)
print(data)
