import numpy as np
import math as m

mat = np.arange(6).reshape(2,3)
a = np.empty(6)
for x in mat.flat:
    a[x] = m.sin(x)
print(a)


mat2 = np.arange(10,16).reshape(2,3)
b = np.empty(6)
i = 0
for y in mat2.flat:
    b[i] = m.cos(y)
    i+=1
print(b)

mat3 = np.add(a,b)
print(mat3)