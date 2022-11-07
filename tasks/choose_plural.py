
def choose_plural(count, string):
    array = string.split(",")
    countArray = []
    result = ""

    b = map(int, str(count))
    for i in b:
        countArray.append(i)

    for x in countArray:
        if x == 1:
            result = array[0]
        elif 2 <= x < 5:
            result = array[1]
        else:
            result = array[2]


    if count == 11:
        result = array[2]

    return result

