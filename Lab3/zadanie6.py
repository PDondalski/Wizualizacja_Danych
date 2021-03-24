import math
def okrag(x, y, a=-1, b=-6):
    return math.sqrt((x-a)**2 + (y - b)**2)
print(okrag(-5, -3))