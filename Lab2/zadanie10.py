import sys
wys = int(sys.stdin.readline())
if wys > 10: 
    print("Wysokość musi być większa od 10")
for x in range(0, wys+1):
    wieza = "A" * x
    print(wieza)