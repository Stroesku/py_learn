# def pyramid_sorting(values):
#

def make_heap(values):
    i = 0
    while i < len(values):
        # перемещение очередного элемента в корень
        index = i
        while index != 0:
            parent_index = (index - 1) // 2

            # Если значение дочернего элемента <= родительскому, то прерываем цикл
            if values[index] <= values[parent_index]:
                break

            # меняем родительский элемент с дочерним
            values[index], values[parent_index] = values[parent_index], values[index]

            # меняем текущий индекс на родителя
            index = parent_index
        i += 1


def remake_heap(values, latest_index):
    index = 0
    while True:
        # вычисляем индексы дочерних элементов
        child1_index = 2 * index + 1
        child2_index = 2 * index + 2

        # если дочерние индексы => последнему индексу то используем родительский
        if child1_index >= latest_index:
            child1_index = index

        if child2_index >= latest_index:
            child2_index = index

        # Если значение родителя больше детей, то выходим из цикла - куча восстановлена
        if (values[index] >= values[child2_index]) and \
                (values[index] >= values[child2_index]):
            break

        # Вычисляем индекс дочернего элемента для обмена
        if values[child1_index] > values[child2_index]:
            swap_child_idx = child1_index
        else:
            swap_child_idx = child2_index

        values[index], values[swap_child_idx] = values[swap_child_idx], values[index]

        # переходим на следующую ветку
        index = swap_child_idx


def heap_sort(values):
    # формируем кучу
    make_heap(values)
    # помещаем элементы корня в конец (по одному за раз)
    i = 0
    while i < len(values):
        last = (len(values) - 1) - i
        # обмениваем
        values[0], values[last] = values[last], values[0]

        # восстанавливаем кучу
        remake_heap(values, latest_index=last - 1)

        i += 1


array = [7, 8, 9, 4, 6, 5, 10, 3, 2, 1]
heap_sort(array)
print("after", array)
