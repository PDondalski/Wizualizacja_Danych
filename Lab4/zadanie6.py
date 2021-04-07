class Slowa:
    def __init__(self, slowo_jeden, slowo_dwa):
        self.slowo_jeden = slowo_jeden
        self.slowo_dwa = slowo_dwa
    def czy_palindrom(self):
        if self.slowo_jeden == self.slowo_jeden[::-1]:
            print(f"{self.slowo_jeden} to palindrom")
    def czy_metagramy(self):
        rozne = 0
        if len(self.slowo_jeden) == len(self.slowo_dwa):
            for x in range(len(self.slowo_jeden)):
                if self.slowo_jeden[x] != self.slowo_dwa[x]:
                        rozne += 1
        if rozne == 1:
            print("Wyrazy są metagramami")
        else: 
            print("Wyrazy nie są metagramami")
    def czy_anagramy(self):
        if sorted(self.slowo_jeden) == sorted(self.slowo_dwa):
            print(f'{self.slowo_jeden} i {self.slowo_dwa} to anagramy')
        else:
            print(f'{self.slowo_jeden} i {self.slowo_dwa} to nie są anagramy')
    def wyswietl_wyrazy(self):
        print(f'{self.slowo_jeden}, {self.slowo_dwa}')
obiekt = Slowa("tama", "mata")
print(obiekt.czy_anagramy())
print(obiekt.wyswietl_wyrazy())