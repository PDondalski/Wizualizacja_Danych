class Kwadrat:
    def __init__(self, x):
        self.x = x
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    def __add__(self, other):
        return self.x + other
    def __ge__(self, other):
        return self.x >= other
    def __gt__(self, other):
        return self.x > other
    def __le__(self, other):
        return self.x <= other
    def __lt__(self, other):
        return self.x < other
kwadrat1 = Kwadrat(5)
kwadrat2 = Kwadrat(6)
inny_kwadrat = kwadrat1.__add__(kwadrat2)
if kwadrat1.__ge__(kwadrat2):
    print("Kwadrat1 jest większy lub taki sam")
if kwadrat1.__gt__(kwadrat2):
    print("Kwadrat1 jest większy")
if kwadrat1.__le__(kwadrat2):
    print("Kwadrat2 jest większy lub taki sam")
if kwadrat1.__lt__(kwadrat2):
    print("Kwadrat2 większy")