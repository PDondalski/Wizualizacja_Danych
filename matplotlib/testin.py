import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2,4,6,8]
'''plt.plot(x,y, label='2x', color='red', linewidth=3, marker='.', markersize=20, markeredgecolor='blue', linestyle='--') '''
# Dodanie koloru poprzez 'color='; pogrubienie linii przez 'linewidth='; 
# Dodanie kropek na wykresie poprzez 'marker=' i zmiana ich rozmiaru poprzez 'markersize=10';
# Zmiana koloru krawędzi kropek poprzez 'markeredgecolor='
# Zmiana stylu linii poprzez 'linestyle='

#ZMIANA WIELKOŚCI GRAFU
plt.figure(figsize=(5,3), dpi=100) # dpi wpłynie na jakość grafu (widoczność pikseli)


'''plt.plot(x,y, 'r.-', label='2x')'''
# 'r.-' - "r" - czerwony kolor, "." - kropki jako punkty, "-" - linia prosta
'''plt.plot(x,y, 'r.--', label='2x')'''
# 'r.-' - "r" - czerwony kolor, "." - kropki jako punkty, "--" - linia kreskowana
'''plt.plot(x,y, 'b^--', label='2x')'''
# 'r.-' - "b" - niebieski kolor, "^" - trójkąty jako punkty, "--" - linia kreskowana
plt.plot(x,y, 'r^--', label='2x')

# Druga linia
x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')
plt.plot(x2[5:], x2[5:]**2, 'r--')
# do pewnego momentu leci linia prosta, a później kreskowana






plt.title('Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize':20}) #Zmiana czcionki i jej rozmiaru
plt.xlabel('X Axis!')
plt.ylabel('Y Axis!')

#Zmiana stylu opisu osi X i Y
plt.xticks([0,1,2,3]) #zmiana skali osi x (na osi x będą liczby 0,1,2,3)
#plt.yticks([0,2,4,6,8,10]) #zmiana skali osi y (tak samo jak w przypadku osi x, tylko te które wpisaliśmy w nawias)


#DODAWANIE LEGENDY
plt.legend() # Dodanie legendy do wykresu, wymaga dodania 'label=' do 'plt.plot(x,y)', a po znaku równości piszemy jak chcemy zapisać tą prostą.

#ZAPISYWANIE GRAFU
plt.savefig('mygraph.png', dpi=300)

#WYŚWIETLENIE GRAFU
plt.show()
