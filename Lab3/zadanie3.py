produkty = {"jabłka": "kg",
            "pomelo": "sztuki",
            "pomarańcze": "kg",
            "awokado": "sztuki"}
odwrocone = {value: key for key, value in produkty.items()}
sztuki = [odwrocone["sztuki"] for x in odwrocone]
print(produkty)
print(odwrocone)
print(sztuki)