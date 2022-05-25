class Eredmenyek:
    nev:str
    kategoria:str
    rajtszam:int
    idoeredmeny: str
    tavSzazalek: int
    def __init__(self, sor: str) -> None:
            adatok=sor.split(';')
            self.nev=adatok[0]
            self.rajtszam=int(adatok[1])
            self.kategoria=adatok[2]
            self.idoeredmeny=adatok[3]
            self.tavSzazalek=int(adatok[4])
file = open("ub2017egyeni.txt","r")
#első sort beolvasom hogy a 2.-ra ugorjon a mutató(az első sor csak fej)
file.readline()
szamlalo = 0
for sor in file:
    #print(sor)
    egyAdat = Eredmenyek(sor)
    print("Neve: ", egyAdat.nev, "ideje:", egyAdat.idoeredmeny)
    if egyAdat.kategoria == "Noi":
        szamlalo += 1
print(szamlalo)

#hany szazalékot teljesített a leghamarabb kieső
minSzazalek=100
if egyAdat.tavSzazalek > minSzazalek:
    minSzazalek=egyAdat.tavSzazalek
    print(minSzazalek)

