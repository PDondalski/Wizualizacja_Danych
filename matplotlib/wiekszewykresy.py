import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,5))

plt.title('Gas Prices over Time (in USD)') #Tytuł wykresu


#plt.plot(gas.Year, gas.USA, 'b.-', label="USA",) #Jeśli chcemy umieścić punkty na wykresie można to zrobić krótką notacją np.:'b.-', czyli niebieska kreska, punkty, linia prosta.
#plt.plot(gas.Year, gas.Canada, 'r.-', label="Canada")
#plt.plot(gas.Year, gas['South Korea'], 'g.-', label="South Korea") #Nazwa zamknięta w nawiasach, bo ma więcej niż 1 słowo
#plt.plot(gas.Year, gas.Australia, 'y.-', label="Australia")

for country in gas:
    if country != 'Year':
        plt.plot(gas.Year, gas[country], marker='.')

plt.xticks(gas.Year[::3]) #Wybieramy lata co 3 rok

plt.xlabel('Year') #Etykieta osi X
plt.ylabel('US Dollars') #Etykieta osi Y

plt.legend() #Dodając legendę, trzeba dopisać label do poszczególnych linii wykresu

plt.show()
