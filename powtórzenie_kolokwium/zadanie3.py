lista = [x for x in range(1,26)]
lista2 = [lista[y * 5 : y * 5 + 5] for y in range(int(len(lista) / 5))]
print(lista2)