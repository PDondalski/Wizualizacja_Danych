import sys
sumaCyfr = 0
liczba = int(sys.stdin.readline())
while(liczba != 0):
    sumaCyfr = sumaCyfr + int(liczba % 10)
    liczba = int(liczba / 10)
sys.stdout.write(str(sumaCyfr))