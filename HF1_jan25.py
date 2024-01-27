from datetime import datetime

class Car:
    forgalmazo_neve = "Autókereskedés Kft."

    def __init__(self, modell, gyartasi_ev, szin, ar, rendszam):
        self.modell = modell
        self.gyartasi_ev = gyartasi_ev
        self.szin = szin
        self.ar = ar
        self.__rendszam = rendszam  # Rendszám privát tagként

    def kor(self):
        # Az aktuális év levonása a gyártási évből
        return datetime.now().year - self.gyartasi_ev

    def __str__(self):
        return f"{self.modell} ({self.gyartasi_ev}), {self.szin}, {self.ar} Ft, Rendszám: {self.__rendszam}"

# Car objektumok létrehozása és tárolása listában
autok = [
    Car("Toyota", 2019, "kék", 15000000, "ABC123"),
    Car("Ford", 2020, "fehér", 18000000, "XYZ789"),
    Car("Honda", 2018, "piros", 12000000, "DEF456")
]

# Forgalmazó nevének kiírása
print(f"Forgalmazó neve: {Car.forgalmazo_neve}\n")

# Autók kiírása a listából, és koraik kiírása
for auto in autok:
    print(auto)
    print(f"Életkor: {auto.kor()} év\n")
