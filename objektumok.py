#a Kutya osztály létrehozása

class Kutya:
    nev:str
    fajta:str
    szulIdo: int


    def ugat(self):
        print("Vau vau...")


#Kutya osztályú objektumok létrehozása (példányosítása) -1 konkrét kutya
enKutyam = Kutya("Tyson", "tacskó", 2020)
print("Kutyám neve:",enKutyam.nev)
print("Kora:", 2022-enKutyam.szulIdo)

teKutyad=Kutya("Licsi", "skótjuhász", 2020)
print("A te kutyád", teKutyad.nev, ",fajtája", teKutyad.fajta,"és születési éve", teKutyad.szulIdo)


#a Kutya osztály metódusának hívása
enKutyam.ugat() 