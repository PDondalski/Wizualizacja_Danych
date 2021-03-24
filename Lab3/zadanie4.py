def monot(a):
    if a > 0:
        return 1
    elif a < 0:
        return 2
    else:
        return 3
x = int(input("Podaj współczynnik funkcji \n"))
if monot(x) == 1:
    print("Funkcja jest rosnąca")
elif monot(x) == 2:
    print("Funkcja jest malejąca")
else:
    print("Funkcja jest stała")