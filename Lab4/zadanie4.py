class NaZakupy:
    def __init__(self, nazwa, ilosc, jednostka, cena):
        self.nazwa_produktu = nazwa
        self.ilosc = ilosc
        self.jednostka_miary = jednostka
        self.cena_jed = cena
    def wyswietl_produkt(self):
        print("Nazwa:", self.nazwa_produktu, "Ilość:", self.ilosc, "Jednostka:", self.jednostka_miary, "Cena:", self.cena_jed, "\n")
    def ile_produkt(self):
        print(self.ilosc, " ", self.jednostka_miary)
    def ile_kosztuje(self):
        print(float(self.cena_jed) * self.ilosc)

zakup1 = NaZakupy("Awokado", 4, "szt", 6)
print(zakup1.wyswietl_produkt())
print(zakup1.ile_produkt())
print(zakup1.ile_kosztuje())