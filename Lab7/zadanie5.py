import numpy as np
import math as m
mat = np.arange(6).reshape(2,3)

a = np.empty(6)
for x in mat.flat:
    a[x] = m.sin(x)
print(a)