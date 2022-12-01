from functools import reduce

# create factorial func
# factorial(n) = 1*2*3...*n

l = range(1, 6)


def mult(x, y):
    return x * y


factorial = reduce(mult, l)
# ----------------------------------------------------
gamers = [
    {"name": "Виктор", "goals": 7, "pass": 5},
    {"name": "Олег", "goals": 6, "pass": 4},
    {"name": "Павел", "goals": 8, "pass": 10},
    {"name": "Халк", "goals": 13, "pass": 14},
]


def goal_pass(gamer):
    return {"name": gamer["name"], "gp": gamer["goals"] + gamer["pass"]}


gamers2 = list(map(goal_pass, gamers))


def best_gamer(gamer1, gamer2):
    if gamer1["gp"] > gamer2["gp"]:
        return gamer1
    return gamer2


print(reduce(best_gamer, map(goal_pass, gamers)))
