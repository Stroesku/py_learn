l1 = [1, 2, 3]
l2 = [5, 6, 7, 8]

print(list(map(lambda t: t[0] * t[1], zip(l1, l2))))  # [5, 12, 21]
