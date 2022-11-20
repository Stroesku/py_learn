l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(x):
    return x * x

l_square = map(square, l)

print(l)
print(list(l_square))
