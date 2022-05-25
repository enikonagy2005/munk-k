#Az ultrabalaton feladatban megadott fájlt olvassuk be 2D listába
file = open("ub2017egyeni.txt","r", encoding="utf-8")
lista=[]
file.readline()
for sor in file:
    egyadat=sor.strip().split(";")
    lista.append(egyadat)