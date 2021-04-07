class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data) - 1 < self.index:
            raise StopIteration
        text = self.data[self.index]
        self.index += 2
        return text
kolekcja1 = Parzyste("Helikopter")
print(kolekcja1.__next__())
print(kolekcja1.__next__())
print(kolekcja1.__next__())
print(kolekcja1.__next__())
print(kolekcja1.__next__())