#1. feladat: Kérd be egy felhasználótól, hogy az úszómedencéje hány cm mély. Ha 150-nél nagyobb, írd ki neki: 
#"A medencéd ... cm mély, tehát mély víz!". Ha kisebb, akkor a következőt: "A medencéd ... cm mély, tehát nem mély víz.". 
#Ha pont 150 cm, Akkor azt a választ kapja, hogy "A medencéd éppen 150 cm mély."

from operator import ge


medence=int(input("Add meg a medencéd mélységét:"))
if medence>150:
    print("A medencéd", medence, "cm mély, tehát mély víz!")
if medence<150:
    print("A medencéd" ,medence, "cm mély, tehát nem mély víz.")
else:
    medence=150
    print("a", medence, " medencéd éppen 150 cm mély")


 #feladat: Kérje be a program egy osztály diákjainak életkorát addig, amíg az életkornak 0-t nem adunk meg. 
 #Minden diákról döntsd el egy függvény segítségével, hogy nagykorú-e. 
 # A függvény paraméterként az életkort kapja meg, 
 # visszatérési értéke pedig logikai érték legyen. 
 #Ez alapján legyen a kiírás: "Nagykorú." vagy "Nem nagykorú."
def nagykoru(eletkor):
    return eletkor>17
eletkor=1
while eletkor!=0:
    eletkor=int(input("A következő diák kora:"))
    if nagykoru(eletkor):
        print("Nagykorú")
    else:
        print("Nem nagykorú")
print("Vége")

#3. feladat: A forrásfájl egy közúti ellenőrzésen áthaladó gépjárművek rendszámát és az időpontokat tartalmazza. 
# Olvasd be a jarmu.txt
#állományt és mentsd el egy megfelelő adatszerkezetben.  
class Gepjarmu:
    ora:int
    perc:int
    mp:int
    rendszam:str
def __init__(self, sor: str) -> None:
    adatok=sor.split(';')
    self.ora=adatok[0]
    self.perc=adatok[1]
    self.mp=adatok[2]
    self.rendszam=int(adatok[3])
file=open("jarmu.txt", "r")

# A szöveges állományban lévő első fejléc sort hagyd figyelmen kívül vagy ugord át.
file.readline()

#Állapítsd meg és írasd ki, hogy összesen hány jármű adata van a szöveges fájlban.


#Hány autó haladt át 9 és 10 óra között



#Van-e Q betűvel kezdődő rendszám
file.seek(0)
file.readline()
szerepele = False
for sor in file:
    Rendszam=Gepjarmu(sor.strip())
    if("Q" in Rendszam.rendszam):
         szerepele = True
if (szerepele):
     print("Van a listában Q nevű rendszám.")  
else:
    print("Nem szerepel a listában Q nevű rendszam.")


#Mikor haladt át az utolsó autó (időrendben vannak)
