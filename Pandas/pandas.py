import pandas as pd #Import biblioteki pandas i zapisanie jej w skrócie "pd", żeby nie pisać później całego "pandas" tylko "pd".
#WCZYTANIE PLIKU CSV DO PROGRAMU. 
#W przypadku formatu csv będzie to -> df = pd.read_csv('pokemon_data.csv')
#print(df.head(3)) - wyświetlanie pierwszych 3 rzędów z bazy. Dokładniej chodzi o 3 rzędy licząc od góry (WERSJA PLIKU CSV)
#print(df.tail(3)) - wyświetlanie ostatnich 3 rzędów z bazy. Dokładniej chodzi o 3 rzędy licząc od dołu (WERSJA PLIKU CSV)

#WCZYTYWANIE PLIKU EXCEL DO PROGRAMU.
#W przypadku formatu xls będzie to -> df_xlsx=pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx.head(3)) - (WERSJA PLIKU EXCELOWEGO)
#print(df_xlsx.tail(3)) - (WERSJA PLIKU EXCELOWEGO)

#WCZYTYWANIE PLIKU .TXT DO PROGRAMU. (ODDZIELONE TABULACJĄ)
#df = pd.read_csv('pokemon_data.txt', delimiter='\t') 
#                                     ^^^^^^^^^^^^^^^
# Delimiter (separator) definiuje jak zostały odzielone od siebie dane, w tym przypadku tabulacja, czyli '\t'
#Inne separatory: np: 'xxx'. <- w miejsce '' wpisujemy separator który został zastosowany w pliku txt
#WYWOŁANIE:
#df = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df.head(3))
'''
Wczytanie pliku csv:
df = pd.read_csv('pokemon_data.csv')
print(df.head(5))
Wczytanie pliku excel:
df = pd.read_excel('pokemon_data.xlsx')
print(df.head(5))
Wczytanie pliku txt:
df = pd.read_csv('pokemon_data.txt', delimiter='\t')
print(df.head(5))
'''
df = pd.read_csv('pokemon_data.csv')
#WYPISANIE NAGŁÓWKÓW KOLUMN
#print(df.columns)

#WYPISANIE KONKRETNEJ KOLUMNY
#print(df['Name']) <- wypisanie kolumny 'Name'
#print(df.Name) <- Inny sposób wyświetlenia kolumny 'Name', ALE DZIAŁA TYLKO W PRZYPADKU NAZWY ZAWIERAJĄCEJ 1 SŁOWO
#print(df['Name'][0:5]) <- wypisanie kolumny 'Name', ALE TYLKO 5 PIERWSZYCH REKORDÓW

#WYPISANIE KILKA KOLUMN NA RAZ
#print(df[['Name', 'Type 1', 'HP']])

#WYPISANIE POSZCZEGÓLNEGO WIERSZA
#print(df.iloc[1]) <- stosujemy parametr 'iloc' (integer location), który wypisuje wiersz przypisany pod podaną przez nas cyfrę
#print(df.iloc[1:4]) <- możemy też wypisać zakres wierszy, w tym przypadku od 2-giego (iteracja zaczyna się od 0) do 3

#WYPISANIE KONKRETNEJ LOKALIZACJI WIERSZA
#print(df.iloc[2,1]) <- 2 - odpowiada za numer wiersza, 1 - odpowiada za numer kolumny.
#print(df.iloc[0,1]) <- inny przykład

#PRZEPATRYWANIE KAŻDEGO WIERSZA PO KOLEI
#for index, row in df.iterrows(): <- pętla która znajdzie każdy indeks i wiersz w pliku i wypisze go po kolei. (iterrows - itarate through rows, czyli przejdź przez wszystkie wiersze)
#    print(index,row) <- wypisanie wszystkich indeksów i wierszy

#PRZEPATRYWANIE KAŻDEGO WIERSZA I WYBIERANIE KONKRETNYCH DANYCH
#for index, row in df.iterrows():
#    print(index, row['Name']) <- zawężamy zakres do 'Name', czyli wyświetlą się same indeksy wraz z przypisanymi do nich nazwami pokemonów.
#print(df.loc[df['Type 1'] == "Fire"]) <- szukamy konkretnych danych. W kolumnie 'Type 1' szukamy wszystkich pokemonów o typie 'Fire'.

#SZYBKIE OTRZYMYWANIE WARTOŚCI (MEAN, STD, MIN, 25%, 50%, 75%, MAX)
#print(df.describe())

#SORTOWANIE WARTOŚCI
#print(df.sort_values('Name')) <- sortuje dane po imieniu, alfabetycznie od A
#print(df.sort_values('Name', ascending=False)) <- sortuje dane po imieniu, alfabetycznie ale od Z (ascending - rosnąco, więc gdy damy '=False', będzie malejąco)
#print(df.sort_values(['Type 1', 'HP'])) <- wypisuje wszystkie dane wg. kryteriów. W tym przypadku bierze pod uwagę najpierw typ alfabetycznie i wtedy po posortowaniu sortuje dodatkowo HP od najmniejszego
#print(df.sort_values(['Type 1', 'HP'], ascending=False)) <- sortuje wg kolumn 'Type 1' i 'HP', obie malejąco
#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0])) <- sortuje obie kolumny oddzielnie. 1 - rosnąco (True) 0 - malejąco (False)

#!!!!DOKONYWANIE ZMIAN W DANYCH!!!!

#DODAWANIE KOLUMNY ("GORSZY SPOSÓB"):
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] <- Dodawanie nowej kolumny 'Total', poprzez dodanie wartości z wszystkich innych kolumn danego wiersza.
#print(df.head(5))

#USUWANIE KOLUMNY:
#df = df.drop(columns=['Total']) <- usuwanie kolumny i przypisanie jej z powrotem do dataframe'u.
#print(df.head(5)) <- wyświetlenie danych po zmianach

#DODAWANIE KOLUMNY (LEPSZY SPOSÓB):
#df['Total'] = df.iloc[:, 4:10].sum(axis=1) <- pierwszy dwukropek oznacza, że chcę wziąć wszystkie wiersze. Po przecinku określamy jakie kolumny chcemy do siebie dodać. W tym przypadku jest to od 4 kolumny do 9, a wpisaliśmy 10, ponieważ 10 parametr jest ostatnim i tym, którego nie wliczamy.
#                              ^^^^^^^^^^^
#Na końcu możemy dopisać '.sum()' a w nawiasie określić, jak chcemy dodawać; 1 - horyzontalnie (poziomo), czy 0 - wertykalnie (pionowo)
#PRZYKŁAD Z WYŚWIETLENIEM:
#df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#print(df.head(5))

#ZMIANA KOLEJNOŚCI KOLUMN:
#df['Total'] = df.iloc[:, 4:10].sum(axis=1) #<- Dodanie kolumny 'Total'
#cols = list(df.columns.values) #<- stworzenie ze wszystkich kolumn listy
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]] #<- przesunięcie kolumn. -1 jest dlatego, bo bierzemy ostatnią kolumnę, jest dodatkowo oprawiona w nawias kwadratowy, ponieważ jako jedyna jest jedną wartością, a nie zakresem.
#print(df.head(5)) <- wypisanie

#!!!!ZAPISANIE ZMIAN DO PLIKU!!!!!
#df.to_csv('modified.csv', index=False) <- zapisuje dane po zmianach do pliku .csv i poprzez dodatkowy parametr 'index=False' nie zapisuje indeksów.
#df.to_excel('modified.xlsx', index=False) <- zapisuje dane do pliku .xlsx (excel)
#df.to_csv('modified.txt', index=False, sep='\t') <- zapisuje dane do pliku .txt i oddziela je tabulatorem. UWAGA! W przypadku zapisu do pliku nie piszemy 'delimiter' jako określenie metody separacji tylko 'sep=' i wpisujemy metodę, w przypadku tabulacji jest to '\t'

#!!!!FILTROWANIE DANYCH!!!!!
#print(df.loc[df['Type 1'] == "Grass"]) <- filtrujemy dane takie, gdzie w 'Type 1' mamy wartość "Grass"
#print(df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison")]) <- Wybieramy takie dane, gdzie w 'Type 1' jest "Grass" i jednocześnie w 'Type 2' jest "Poison". W przypadku filtrowania używamy spójników logicznych typu '&,|' zamiast 'and, or'
#print(df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison") & (df['HP'] > 70)]) <- filtrujemy nie tylko po wybraniu konkretnej nazwy, ale też możemy podać zakres liczbowy w danej kolumnie.

#ZAPIS DO NOWEGO DATAFRAME
#new_df = df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison") & (df['HP'] > 70)]
#new_df.to_csv('filtered.csv') <- zapis nowego dataframe do pliku
#new_df = new_df.reset_index() <- resetuje indeksy tylko w nowej kolumnie i zapisuje stare
#new_df = new_df.reset_index(drop=True) <- usuwa stare indeksy, a dodaje nowe
#new_df.reset_index(drop=True, inplace=True) <- jeśli nie chcemy resetować indeksów do nowej zmiennej dataframe, możemy zrobić to lokalnie dopisując 'inplace=True'.

#WYSZUKIWANIE REKORDÓW KTÓRE ZAWIERAJĄ JAKIEŚ SŁOWO
#print(df.loc[df['Name'].str.contains('Mega')]) <- wyszukuje wszystkie nazwy pokemonów, które mają w nazwie 'Mega'.
#print(df.loc[~df['Name'].str.contains('Mega')]) <- wyszukuje wszystkie nazwy które NIE MAJĄ w nazwie 'Mega'.

#ZMIANY W DANYCH
#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer' <- podmienia nazwę 'Fire' na 'Flamer'
#df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire' <- zmienia z powrotem
#df.loc[df['Type 1] == 'Fire', 'Legendary'] = True <- powoduje, że wszystkie pokemony 'Fire' są teraz legendarne. UWAGA! Nie da się tego cofnąć.

#ZMIANY W WIELU MIEJSCACH NA RAZ
#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE' <- wszędzie, gdzie wartość 'Total' jest >500 pojawi się napis 'TEST VALUE' w kolumnach 'Generation' i 'Legendary'
#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2'] <- teraz pod 'Generation' będzie 'Test 1', a pod 'Legendary' będzie 'Test 2', jeśli zostaną spełnione warunki opisane wyżej.

#!!!!!GROUP BY!!!!!
#print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)) <- wypisuje średnią wartości 'Defense' i sortuje od największej do najmniejszej.
#print(df.groupby(['Type 1']).sum()) <- sumuje wszystkie wartości wg podanego parametru.
#print(df.groupby(['Type 1']).count()) <- liczy wszystkie wartości wg parametru.

#PODAJE TYLKO ILOŚĆ POKEMONÓW DANEGO TYPU
#df['count'] = 1
#print(df.groupby(['Type 1']).count()['count'])

#PODAJE ILE JEST TYPE2 W TYPE1, CZYLI WYPISUJE TYPY POKEMONÓW I ICH TYPY WEWNĘTRZNE
#df['count'] = 1
#print(df.groupby(['Type 1', 'Type 2']).count()['count'])

#print(df)












