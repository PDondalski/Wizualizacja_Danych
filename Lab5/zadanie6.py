class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
kolekcja1 = Wspak("Helikopter")
for i in range(kolekcja1.index):
    print(kolekcja1.__next__())
print("\n")
kolekcja2 = Wspak("Akwamaryna")
for x in range(kolekcja2.index):
    print(kolekcja2.__next__())