def getMinValueViaFor(list):
    if not list: return 0
    minValue = list[0]
    for item in list[1:]:
        if item < minValue:
            minValue = item
    return minValue


def getMinValueViaWhile(list):
    if not list: return 0
    minItem = list[0]
    firstIndex = 0

    while firstIndex < len(list):
        if list[firstIndex] < minItem:
            minItem = list[firstIndex]
        firstIndex += 1
    return minItem


# Implementation via while
firstArray = [23, 4, 7, 4, 12, 6, 8, 41, 20]

# Implement via for
secondArray = []


def line(length):
    string = '-'
    repeatedLine = string * length
    return repeatedLine


print(line(15))

x = int(input())
print(type(x))

