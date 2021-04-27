import numpy as np
w1 = "mama"
w2 = "mata"
w3 = "mózg"
mat1 = np.diag(list(w1))
mat1[0:4,0]=list(w3)
mat1[0,0:4]=list(w2)
print(mat1)