from posixpath import split
from pydoc import stripid


file=open('orvosi_nobeldijak.txt', 'r', encoding='utf_8')
lista=[]
file.readline()
for sor in file:
    lista.append(sor.strip().split(";"))
print(lista)
print(lista[1] [3])
db=0
for sor in lista:
    if sor[3]=='GB':
        db=db+1
        
print(db)


for sor in lista:
    if int(sor[0])<1905:
        print(sor[1])
        
        
for sor in lista:
    if sor[1] [0] =="A":
        print(sor[1])
        
        
        
for sor in lista:
    if len(sor[2])==5:
        print(sor[1])



