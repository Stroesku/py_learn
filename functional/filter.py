l = [4, 17, 23, 12, 6, 57, 84]


def is_even(j):
    return j % 2 == 0


def gt_10(j):
    return j > 10


list = list(filter(gt_10, filter(is_even,l)))
print(list)
