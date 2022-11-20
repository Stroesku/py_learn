from functools import reduce

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]


def get_room_with_square(room):
    length = room["length"]
    width = room["width"]
    square = length * width
    room["square"] = square
    return room


def get_room_square(room):
    length = room["length"]
    width = room["width"]
    square = length * width
    return square


def get_flat_square(s1, s2):
    result = s1 + s2
    return result

roomSquare = list(map(get_room_square, rooms))
square = reduce(get_flat_square, map(get_room_square, rooms))