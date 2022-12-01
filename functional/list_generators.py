l = range(1, 11)
l2 = list(map(lambda x: x ** 2, l))

l3 = [x ** 2 for x in l]
l4 = [str(x) for x in l if x % 2 == 0]

d = {x: x ** 2 for x in l}

students = [
    {"name": "Светлана", "avg_ball": 4.7},
    {"name": "София", "avg_ball": 5.0},
    {"name": "Егор", "avg_ball": 4.4},
    {"name": "Марина", "avg_ball": 4.2},
    {"name": "Дима", "avg_ball": 3.8},
    {"name": "Антон", "avg_ball": 4.0},
    {"name": "Милана", "avg_ball": 4.9},
    {"name": "Фёдор", "avg_ball": 4.5},
    {"name": "Татьяна", "avg_ball": 3.7}
]

gold = list(x["name"] for x in students if x["avg_ball"] >= 4.9)
silver = list(x["name"] for x in students if 4.5 <= x["avg_ball"] <= 4.8)

print(gold)
print(silver)
