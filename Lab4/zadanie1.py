plik = open("dane.txt","w+")
for x in range(4,100,4):
    plik.write(str(x))
    plik.write("\n")