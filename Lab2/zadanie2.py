import sys
print("Podaj pierwszą liczbę: ")
liczba1 = int(sys.stdin.readline())
print("Podaj drugą liczbę: ")
liczba2 = int(sys.stdin.readline())
wynik = liczba1*liczba2
sys.stdout.write(str(f'Wynik: {wynik}'))