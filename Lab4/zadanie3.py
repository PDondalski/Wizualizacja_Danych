with open("dane2.txt", "w+") as plik: 
    for x in range(1,10,1):
        plik.write("tekst")
        plik.write("\n")
with open("dane2.txt", "r") as plik:
    for linia in plik:
        print(linia)