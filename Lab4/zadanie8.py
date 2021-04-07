class Robot:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow*self.krok

    def __del__(self):
        print("obiekt został zniszczony")

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow*self.krok
    
    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow*self.krok
        
    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow*self.krok
    
    def pokaz_gdzie_jestes(self):
        print(f"Jesteś w punkcie: {self.x}, {self.y}")


test1 = Robot(0,0,1)
test1.idz_w_gore(10)
test1.idz_w_lewo(6)
test1.pokaz_gdzie_jestes()

test2 = Robot(5,5,1)
test2.idz_w_dol(100)
test2.idz_w_prawo(50)
test2.idz_w_lewo(30)
test2.idz_w_dol(55)
test2.pokaz_gdzie_jestes()