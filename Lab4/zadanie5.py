class Ciag:
    ciagi = []
    a1 = None
    n = None
    r = None

    def wyswietl_dane(self):
        for ciag in self.ciagi:
            print(ciag, end="\t")

    def pobierz_elementy(self):
        ciag = int(input("Podaj liczbe: "))
        self.ciagi.append(ciag)

    def pobierz_parametry(self):
        self.a1 = int(input("Podaj a1: "))
        self.n = int(input("Podaj ilosc elementow: "))
        self.r = int(input("Podaj r: "))

    def policz_sume(self):
        return sum(self.ciagi)

    def policz_elementy(self):
        if self.a1 is not None and self.r is not None:
            return len(self.ciagi)

ciag = Ciag()
ciag.pobierz_elementy()
ciag.pobierz_parametry()
print(ciag.policz_sume())
print(ciag.policz_elementy())
ciag.wyswietl_dane()