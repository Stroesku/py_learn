def is_cross(a, b):
    ax1, ay1, ax2, ay2 = a[0], a[1], a[2], a[3]
    bx1, by1, bx2, by2 = b[0], b[1], b[2], b[3]

    aXRange = []
    aYRange = []
    bXRange = []
    bYRange = []

    for x in range(ax1, ax2 + 1):
        aXRange.append(x)

    for y in range(ay2, ay1 + 1):
        aYRange.append(y)

    for x in range(bx1, bx2 + 1):
        bXRange.append(x)

    for y in range(by2, by1 + 1):
        bYRange.append(y)

    commonPointOnX = list(set(aXRange) & set(bXRange))
    commonPointOnY = list(set(aYRange) & set(bYRange))

    return commonPointOnX != [] and commonPointOnY != []
