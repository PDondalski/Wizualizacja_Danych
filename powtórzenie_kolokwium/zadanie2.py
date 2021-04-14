tekst = input("Podaj napis: ")
Wielkie = 0
Male = 0
for x in range(len(tekst)):
    if tekst[x].isupper():
        Wielkie += 1
    elif tekst[x].islower():
        Male += 1
print(f'Małych liter jest: {Male}, a wielkich jest: {Wielkie}.')