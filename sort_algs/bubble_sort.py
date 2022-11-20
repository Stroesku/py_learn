def bubble_sort(values):
    is_sorted = False

    while not is_sorted:
        # Изначально считаем что на текущей итерации массив отсортирован
        is_sorted = True
        n = 1
        print("итерация:", values)

        # перебираем массив
        for i in range(len(values) - n):
            # Сравниваем два элемента: текущий и следующий
            if values[i] > values[i + 1]:
                # делаем своп
                values[i], values[i + 1] = values[i + 1], values[i]
                # отмечаем что массив не отсортирован, это говорит о том что будет нужна еще одна итерация
                is_sorted = False
        n += 1


array = [7, 8, 5, 9, 4, 1]
print(array)
bubble_sort(array)
print(array)
