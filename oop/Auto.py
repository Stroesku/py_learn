class Auto:
    count = 0
    objects = []

    def __init__(self, number=""):
        self._number = number
        self.power = 0
        if number:
            self.number = number

        Auto.count += 1
        Auto.object.append(self)

    @staticmethod
    def set_powers(power):
        for obj in Auto.objects:
            obj.power = power

    @property
    def number(self):
        return "".join(self._number)

    @number.setter
    def number(self, newNumber):
        if newNumber.__len__() != 6:
            print("Номер должен содержать 6 символов")
        else:
            self._number = []
            for i in newNumber:
                self._number.append(i)

    def get_tax(self, min_rate=12, max_rate=25):
        rate = min_rate
        if self.power > 100:
            rate = max_rate
        return rate * self.power

    # или вместо декоратора можно сделать так:
    # number = property(getNumber, setNumber)


class Buss(Auto):
    def get_tax(self, min_rate=15, max_rate=15):
        return super().get_tax(min_rate, max_rate)


class InterCityBus:
    pass
