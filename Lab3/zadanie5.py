def proste(a1, a2):
    if a1 == a2:
        return 1
    elif a1*a2==-1:
        return 2
x = int(input("Podaj a1: \n"))
y = int(input("Podaj a2: \n"))
if proste(x,y) == 1:
    print("Proste są równoległe")
elif proste(x,y) == 2:
    print("Proste są prostopadłe")
print(proste(x,y))