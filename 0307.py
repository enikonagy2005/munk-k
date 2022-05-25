from turtle import st


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
file.readline()
osszesEredmeny: list[Eredmenyek] = []

for sor in file:
    egyEredmeny=Eredmenyek(sor.strip())
    #a létrehozott egyEredmeny hozzáfűzöm a listához
    osszesEredmeny.append(egyEredmeny)
    
print("A listában", len(osszesEredmeny), "eredmény van")


#számolja meg és írja ki a képernyőre a minta szerint, hogy háy nőisportoló teljesítette a távot
file.seek(0)
file.readline()
noidb=0
for adatok in osszesEredmeny :
    if adatok.kategoria== "Noi" and adatok.tavSzazalek==100:
        noidb=noidb +1
        
print("Enyi női versenyző fejezte be a versenyt:" ,noidb)



#kérje be a felhasználótól egy sportó nevét majd határozza meg és írja ki a minta szerint, hogy a sportoló indult e versenyen!
#Ha a sportoló indult a versenyen, akkor azt is írja ki a képernyőre,hogy a teljes távott teljesítette e!




#Irassa ki az első sportoló idejét órában
ido=osszesEredmeny[0].idoeredmeny.split(":")
oraban=(int(ido[0])*3600+int(ido[1])*60+int(ido[2])) /3600
print(oraban)




#készítsünk egy füffvényt(idoOraban)ami megkapja a versenyző időeredményét
#majd visszaadja az időt órában!
def idoOraban(idoString: st)->float:
    ido=idoString.split(":")
      
 


#Határozza meg és írja ki a minta szerint a teljes távot teljesítő
#a férfi sportolók átlagos idejét órában!
osszesFerfi=0
osszIdo=0
for adatok in osszesEredmeny:
    if adatok.kategoria== "ferfi" and adatok.tavszazalek==100:
     osszIdo=osszIdo+idoOraban(adatok.ido)
print(osszesFerfi)
print(osszIdo,"", osszesFerfi)


#hány célba érkezett versenyző van, aki előtti és utáni nem teljesítette a távot
darab=0
for i in range (1,len(osszesEredmeny)-1):
    if osszesEredmeny[i].tavSzazalek==100 and osszesEredmeny[i-1].tavSzazalek < 100 and osszesEredmeny[i+1].tavSzazalek >100:
        darab+=1
        
print(darab)
        

keresztNev=input("Add meg egy sportoló nevét:")

bennevane=False
for egyAdat in osszesEredmeny:
    if egyAdat.nev==keresztNev:
        bennevanr=True
        print("indult")
        if egyAdat.tavSzazalek==100:
            print("végig ment")
        else: print("nem teljesítette")
        
if not bennevane:
    print("nem indult")
    



