#hozz létre egy Autó osztályt


class Auto:
    marka:str
    evjarat:int
    szin:str
    hengerurtartalom:int

    def __init__(self, markaja:str, evjarata:int, szine:str, tartalma:int) -> None:
        self.marka= markaja
        self.evjarat=evjarata
        self.szin=szine
        self.hengerurtartalom=tartalma
    def berreg(self):
        print("Tü tü...")

Autom = Auto("Audi", 2021, "Matt fekete", 1300)
print(Autom.szin)
Autom.berreg()

