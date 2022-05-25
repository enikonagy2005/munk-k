# OSZTÁLY:

class Haromszog:
    a: int
    b: int
    c: int
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])  
#Majd hozz létre egy file változót, amiben a haromszogek.txt állományt nyitod meg olvasásra
file=open("haromszog.txt", "r")

# fájl sorait olvasd be 2D lista adatszerkezetbe.
lista=[]
for sor in file:
    lista.append(sor.strip().split("*"))
print(lista)

#A lista minden eleméből példányosíts egy egyHaromszog nevű, Haromszog típusú objektumot.
for item in lista:
    print(item)
    egyHaromszog=Haromszog(item)
    print(egyHaromszog.haromszoge())
    print(egyHaromszog.kerulet())
    



#Az osztálynak már vannak kész metódusai. A haromszoge() metódus segítségével írasd ki listasoronként
# hogy háromszöget alkotnak-e a számok.



#A kerulet() metódus segítségével írasd ki az egyes háromszögek kerületét.