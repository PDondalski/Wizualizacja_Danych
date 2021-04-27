import numpy as np
def generate(x, y):
    tab = np.logspace(1, y+1, num=y, endpoint=False, base=x)
    return tab
print(generate(3,5))

