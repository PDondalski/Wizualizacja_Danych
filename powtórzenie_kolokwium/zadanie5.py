def ileZnakow(tekst):
    znaki = {i:tekst.count(i) for i in tekst}
    return znaki
print(ileZnakow("Przykładowy Tekst"))