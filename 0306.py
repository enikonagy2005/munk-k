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

#Hány Nobeldíjas van?

file.readline()
nobelDijasok=0
for sor in file:
    nobelDijasok+=1

print("A fájlban", nobelDijasok, "sor van")


#Hány magyar Nobeldíjas van?
file.seek(0)
file.read
magyarDb=0
for sor in file:
    egyEmber=nobelDijasok(sor.strip())
    if(egyEmber.orszag=="H"):
          magyarDb=magyarDb+1


#Mikor kapták az első Nobeldíjat?
file.seek(0)
file.readline()
elsoNobeldij=2022
for sor in file:
    egyEmber=nobelDijasok(sor.strip())
    if (egyEmber.ev<elsoNobeldij):
        elsoNobeldij=egyEmber.ev
          
          


#Szerepel e a listában Archibald nevű ember?
file.seek(0)
file.readline()
szerepele=False
for sor in file:
    egyEmber=nobelDijasok(sor.strip())
    if ("Archibald" in egyEmber.nev):
        szerepele=True
if (szerepele):
    print("Szerepel a listában Archibald nevű díjzott")
else:
    print("Nem szerepel a listában Archibald nevű díjazott")





#Irasd ki soronként, hogy hány éves korban halt meg a díjazott(Hha még él ne írj ki semmit)
file.seek(0)
file.readline()  
for sor in file:
    egyEmber=nobelDijasok(sor.strip())
    evek=egyEmber.szuletesHal.split("-")
    if(evek[1] !=""):
        print(egyEmber, ":", int(evek[1])-int(evek[0]))