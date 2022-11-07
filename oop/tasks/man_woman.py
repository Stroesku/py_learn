class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.lower()


class Man(People):
    def get_sex(self):
        return "m"

class Woman(People):
    def get_sex(self):
        return "w"