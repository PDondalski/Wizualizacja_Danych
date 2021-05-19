import pandas as pd
import numpy as np

plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik)
#print(df)
#print(df[df.Liczba > 1000])

#print(df[df['Imie'] == "PAWEŁ"])
#print(df.agg({'Liczba':['sum']}))
df2 = df[((df.Rok > 2000) & (df.Rok < 2005))]
#print(df2.agg({'Liczba':['sum']}))
#print(df.groupby(['Plec']).agg({'Liczba':['sum']}))

#print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())

print(df.groupby(['Plec', 'Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).iloc[[0,1]])