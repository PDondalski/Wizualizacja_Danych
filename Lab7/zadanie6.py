import numpy as np
import math as m
mat2 = np.arange(10,16).reshape(2,3)
b = np.empty(6)
i = 0
for y in mat2.flat:
    b[i] = m.cos(y)
    i+=1
print(b)