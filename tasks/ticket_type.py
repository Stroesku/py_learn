def ticket_type(ticket_number):
    arrayInt = [int(i) for i in list(str(ticket_number))]
    firstSum = sum(arrayInt[:3])
    lastSum = sum(arrayInt[3:])
    if firstSum == lastSum:
        return "счастливый"
    elif firstSum - lastSum == 1 or firstSum - lastSum == -1:
        return "встречный"
    elif firstSum - lastSum == 2 or firstSum - lastSum == -2:
        return "пьяный"
    else:
        return "обычный"