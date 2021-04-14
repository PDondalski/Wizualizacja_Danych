def najwieksze(lista):
    lista = sorted(lista, reverse=True)
    return lista[:3]
test = [1,3,5,7,10]
print(najwieksze(test))