class Involution:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, value):
        return value ** self.degree


involution = Involution(3)

print(involution(4))
