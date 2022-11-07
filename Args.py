# def line(fill, length=10):
#     repeatedLine = fill * length
#     return repeatedLine
#
#
# print(line(fill="2", length=20))

# -----------------------------------

# rus_president_fn = "Владимир"
# rus_president_ln = "Путин"
# rus_president_p = "Владимирович"
# usa_president = ["Барак", "Обама", "Иванович"]
#
# first_rp = {"last_name": "Ельцин", "first_name": "Борис"}
#
#
# def print_full_name(first_name, last_name, patronymic=""):
#     print(first_name, last_name, patronymic)
#
#
# print_full_name(rus_president_fn, rus_president_ln, rus_president_p)
# print_full_name(usa_president[0], usa_president[1])
# print_full_name(*usa_president)
# print_full_name(**first_rp)


# -----------------------------------
# Vararg
a, b, c = 10, 20, 0


def mult(digits):
    result = 1
    for d in digits:
        result *= d
    return result





def g_mult():
    global c
    c = a * b


def print_dict(**kwargs):
    for item in kwargs.items():
        print(*item, sep=": ")

g_mult()
print(mult(3,3))

# print(mult(10,20,30,40))

fn = "Иван"
ln = "Петров"
p = "Сидорович"
# print_dict(lastname=ln, patronymic=p)
