class Nobeldijasok:
    ev:int
    nev:str
    szuletesHal:str
    orszag:str
    def __init__(self, sor: str) -> None:
        adatok=sor.split(';')
        self.ev=int(adatok[0])
        self.nev=adatok[1]
        self.szuletesHal=adatok[2]
        self.orszag=adatok[3]

#fájl megnyitása
file= open("orvosi_nobeldijak" , "r")

osszesnobeldijasok= list[Nobeldijasok]=[]
for sor in file:
    egyEmber=Nobeldijasok(sor.strip())
    osszesnobeldijasok.append(egyEmber)
    
    
for egy in osszesnobeldijasok:
    print(egy.ev)
    
    
    for i in range(len(osszesnobeldijasok)):
        print(osszesnobeldijasok[i].nev)