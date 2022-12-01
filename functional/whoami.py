from functools import reduce

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']


def concat(a, b):
    return a + b


whoami = reduce(concat, whoami)
print(whoami)