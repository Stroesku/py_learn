from functools import reduce

# create factorial func
# factorial(n) = 1*2*3...*n

l = range(1, 6)


def mult(x, y):
    return x * y


factorial = reduce(mult, l)
