import random
macierz = [[random.random() for j in range(4)] for i in range(4)]
przekatna = [macierz[x][x] for x in range(4)]
print(przekatna)