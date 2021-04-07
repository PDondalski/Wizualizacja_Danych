class Samogloski:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
        else:
            return "String nie został przekazany"
    def __iter__(self):
        return self
    def __next__(self):
        data2 = []
        samog = ["a", "e", "i", "o", "u", "y"]
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if(self.data[i] == samo[j]):
                    return self.data[i]
kolekcja1 = Samogloski("Helikopter")
print(kolekcja1.__next__())
print(kolekcja1.__next__())