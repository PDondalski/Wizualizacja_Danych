import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


labels = ['A', 'B', 'C']
values = [1,4,2]

bars = plt.bar(labels, values)

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
#bars[0].set_hatch('/') # Dodanie na wykres słupkowy kresek
#bars[1].set_hatch('O')
#bars[2].set_hatch('*')

#plt.figure(figsize=(6,4))

plt.show()