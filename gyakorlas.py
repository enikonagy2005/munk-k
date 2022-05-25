#nyissuk meg a fájlt
list = []
file=open("haromszogek.txt",'r')
for sor in file:
    print(sor)
file.seek(0,0)

sor1=file.readline().strip()
list.append(sor1)
print(list)


#irassuk ki a második sort
print(file.readline())



#a harmadik sorban lévő számokat listázzuk be
sor3=file.readline().split()
list=sor3
print(list)

#irassuk ki a legnagyobb szamot
print(max(list))


#irassuk ki a lista második elemét
print(list[1])

ki=open("ki.txt", "w")
ki.write(list[1])


#adjuk meg hogy négyszer fusson le és írjuk is ki a sorokat
file.seek(0,0)
for i in range(4):
    print(i)

print("alma")    