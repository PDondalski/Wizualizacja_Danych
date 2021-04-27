import numpy as np
def function(n):
    list = [x for x in range(1,n*n+1)]
    a = np.array([list[y * n : y * n + n] for y in range(int(len(list) / n))])
    return a
print(function(5))