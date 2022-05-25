# Írasd ki az összes sort
from asyncore import write


file=open("adatok.txt" , "r")
for f in file:
     print(f)

# Olvasd be a fájl első sorát, amely megadja, hogy összesen hány adatsor van.    
file.seek(0,0)
sor= file.readlines()
print(sor)

# Írasd ki egy sorokszama.txt fájlba a sorok számát. 
sorokszama=open("adatok.txt", "w")
sorokszama.write(sorokszama.readline())




# Írasd ki külön az adatsorokat és külön az összes sorok számát.




# a sorokban levő 3 szám szorzatát írd ki. Csak az adatsorokkal dolgozz!