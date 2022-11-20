def insert_sort(array):
    start = 1
    while start < len(array):
        previous = start - 1
        while array[previous + 1] < array[previous] and previous >= 0:
            array[previous + 1], array[previous] = array[previous], array[previous + 1]
            previous -= 1
        start += 1


a = [7, 8, 9, 4, 6, 5, 10, 3, 2, 1]
insert_sort(a)
print(a)
