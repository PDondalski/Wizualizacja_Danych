a = int(input("Podaj a:\n"))
b = int(input("Podaj b:\n"))
c = int(input("Podaj c:\n"))
if (a > 0 and a <= 10) and (a > b or b > c):
    print("Warunki spełnione\n")
else:
    print("Warunki nie spełnione")