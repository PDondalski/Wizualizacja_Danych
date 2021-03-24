def lista_zakupow(** zakupy):
    suma = 0.0
    for i in zakupy:
        suma += zakupy[i]
    return suma
print("Liczba produktów na liście: ", lista_zakupow(banany=10, jabłka=20))