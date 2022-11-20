def merge_sort(array):
    temp_array = [None] * len(array)

    do_mergesort(array, temp_array, 0, len(array) - 1)


def do_mergesort(array, temp_array, start, end):
    if start == end:
        return

    midpoint = (start + end) // 2
    do_mergesort(array, temp_array, start, midpoint)
    do_mergesort(array, temp_array, midpoint + 1, end)

    # Слияние двух отсортированных массивов
    left_index = start
    right_index = midpoint + 1
    temp_array_index = left_index
    while (left_index <= midpoint) and (right_index <= end):
        if array[left_index] <= array[right_index]:
            temp_array[temp_array_index] = array[left_index]
            left_index += 1
        else:
            temp_array[temp_array_index] = array[right_index]
            right_index += 1
        temp_array_index += 1

    # Финальное копирование непустых массивов.
    for i in range(left_index, midpoint + 1):
        temp_array[temp_array_index] = array[i]
        temp_array_index += 1

    for i in range(right_index, end + 1):
        temp_array[temp_array_index] = array[i]
        temp_array_index += 1

    for i in range(start, end + 1):
        array[i] = temp_array[i]


data = [8, 7, 2, 4, 9, 6, 1, 5, 3, 10]
merge_sort(data)
print(data)
