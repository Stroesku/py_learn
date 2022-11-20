from functools import reduce

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']


def concate(a, b):
    return a + b


whoami = reduce(concate,whoami)
print(whoami)