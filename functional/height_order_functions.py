l = [4, 17, 23, 12, 6, 57, 84]


def is_even(j):
    return j % 2 == 0


def my_filter(predicate_fun, values):
    new_values = []
    for i in values:
        if predicate_fun(i): new_values.append(i)
    return new_values


l2 = my_filter(lambda j: j % 2 == 0, l)

print(l2)
