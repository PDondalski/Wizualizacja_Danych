# Za pomocą python comprehensions (wyrażenie listowe) wygeneruj ciąg 12 kolejnych potęg liczby 2 poczynając od
# wykładnika = 1
print([2 ** i for i in range(12)])


# Napisz skrypt/funkcję, która zlicza ilość wielkich i małych liter w ciągu tekstowym podanym jako parametr wejściowy
# i wyświetla ich ilość na ekranie.
def letter_count(text):
	lower_count = 0
	upper_count = 0

	for i in range(len(text)):
		if text[i].isupper():
			upper_count += 1

		if text[i].islower():
			lower_count += 1

	print("Małe litery: {}\nDuże litery: {}".format(lower_count, upper_count))


letter_count("Jakiś tam tekst")

# Wygeneruj listę 25 kolejnych liczb (rozpoczynając od 1) i korzystając z pętli for wygeneruj z niej listę dwupoziomową
# 5x5
numbers = [i for i in range(1, 25 + 1)]
print(numbers)
numbers_two_level = [numbers[i * 5:i * 5 + 5] for i in range(int(len(numbers) / 5))]
print(numbers_two_level)

# Napisz funkcję, która będzie zwracała 3 największe wartości z listy numerycznej.
def three_big_numbers(l):
	new_l = sorted(l, reverse=True)

	return new_l[:3]

print(three_big_numbers([1, 3, 6, 13, 12]))

# Napisz funkcję, która będzie przyjmowała tekst jako parametr wejściowy a następnie w słowniku będzie zapisywała
# ilość poszczególnych znaków w podanym tekście (znak klucz – ilość to wartość). Wyświetl wyniki na ekranie
def char_count(text):
	output = {i:text.count(i) for i in list(set(text))}

	return output

print(char_count("Jakiś tam tekst"))

# Napisz funkcję, która odczyta plik z kolejnymi wartościami liczbowymi (przygotuj plik) zapisanymi po jednej w wierszu
# a następnie do tego samego pliku zapisze te wartości posortowane rosnąco (również po jednej w wierszu).
def sort_number_in_file():
	with open('file.txt', 'r+') as f:
		n = [int(i) for i in f.read().split()]
		f.seek(0)
		f.write('\n'.join([str(i) for i in sorted(n)]))

sort_number_in_file()

# Napisz funkcję, która przyjmuje 2 parametry: ‘ile’ oraz ‘przedzial’ (krotka)
# Funkcja losuje liczby (ile) z podanego przedziału (przedzial np. krotka (1,100)) i wyświetla sumę tych liczb oraz ich
# średnią arytmetyczną.
import random
def sum_avg(ile, przedzial):
	random.seed()
	num = [random.randint(*przedzial) for i in range(ile)]
	print(num)
	print("Suma: {}\nŚrednia: {}".format(sum(num), sum(num) / len(num)))

sum_avg(5, (1, 100))

# Napisz funkcję/skrypt, który:
# - jako parametr wejściowy pobiera zdanie wpisywane z klawiatury,
# - ponownie z klawiatury pobiera nazwę pliku, w którym zapisany zostanie wynik działania funkcji,
# - do pliku zapisywane są unikalne wyrazy ze zdania pisane małymi literami po jednym w linii,
# - ze zdania zostaną usunięte ewentualne przecinki i kropki
def file_quest(text):
	# file_name = input("Wprowadź nazwę pliku: ")
	file_name = 'nazwa.txt'

	text = text.lower()

	txt_list = text.replace('.', '').replace(',', '').split(' ')

	with open(file_name, 'w') as f:
		f.write('\n'.join([word for word in txt_list if txt_list.count(word) == 1]))

# text = input("Wprowadź tekst:")
text = 'Ala ma kota. ala'
file_quest(text)