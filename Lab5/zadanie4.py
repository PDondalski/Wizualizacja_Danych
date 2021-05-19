class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(1,3)
p4 = Point(3,6)
p2.update(3)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)