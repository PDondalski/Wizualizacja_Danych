zdanie = input("Podaj zdanie \n")
def funkcja(zdanie):
    nazwa = input("Jak ma się nazywać plik? \n")
    zdanie = zdanie.lower()
    zdanie = zdanie.replace(",",'').replace(".",'').split(' ')
    with open(nazwa + ".txt", 'w') as p:
        p.write('\n'.join([word for word in zdanie]))
funkcja(zdanie)