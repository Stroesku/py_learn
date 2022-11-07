def floor(number, sumFlat):
    # contain array of flatNumber per floor
    floorList = []
    flatsBuffer = []
    counter = 0
    for f in range(1, number + 1):
        counter = counter + 1
        flatsBuffer.append(f)
        if f == number: floorList.append(flatsBuffer)
        elif counter == sumFlat:
            floorList.append(flatsBuffer.copy())
            flatsBuffer.clear()
            counter = 0

    print(floorList)
    for floor in floorList:
        for flat in floor:
            if flat == number: return floorList.index(floor) + 1
    else: return "Квартира не найдена"


print(floor(8, 4))
