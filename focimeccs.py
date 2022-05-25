#olvassuk be az adatokat


class Eredmény:
    fordulo:int
    hazaigol:int
    vendeggol: int
    hazaifelidogol:int
    vendegfelidogol: int
    hazaicsapat: str
    vendegcsapat:str
    
    def __init__(self, sor: str) -> None:
        adatok=sor.strip().split(' ')                                                                               
         self.fordulo=int(adatok[0])
         self.hazaigol=int(adatok[1])
         self.vendeggol=int(adatok[2])
         self.hazaifelidogol=int(adatok[3])
         self.vendegfelidogol=int(adatok[4])
         self.hazaicsapat=adatok[5]
         self.vendegcsapat=adatok[6]
            
file = open("meccs.txt","r")
file.readline()
lista: list[Eredmény]=[]
for i in file:
    lista.append(Eredmény(i))
#irassa ki hány mérkőzés van a listában összesen
print(len(lista))






#2 feladat
bekeres=int(input("Adj meg egy számot 1-20 között:"))
for i in lista:
    if i.fordulo==bekeres:
        print(i.hazaicsapat,i.vendegcsapat,i.hazaigol,i.vendeggol,i.hazaifelidogol,i.vendegfelidogol)
    
        

#kérjünk be egy csapat nevet és válaszoljon van e benne
vane=False
csapat=input("Adj meg egy csapat nevet:")
for i in lista:
    if i.hazaicsapat==csapat or i.vendegcsapat==csapat:
        vane=True
    else:
        vane=False
if (vane):
    print("van")
else:
    print("nincs")


#Mikor volt olyan, hohy sikerült megfordulnia az állásnak






#hány gólt lőttek a nyulak vendég pályán
osszgol=0
for i in lista:
    if lista.vendegcsapat =="Nyulak":
        osszgol=osszgol+lista.vendeggol
print("A Nyulak csapat",osszgol,"golt lőtt idegenben")
  









