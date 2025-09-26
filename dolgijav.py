lista=[2,4,1,8,3]
#A.1 lista elemeinek összege
osszeg=0
for i in lista:
    osszeg += i
print(f"{osszeg}")
print(f"{sum(lista)}")
#A.2 lista elemeinek összege
paros_osszeg=0
paros_darab=0
for szam in lista:
    if szam%2==0:
        paros_darab+=1
        paros_osszeg+=szam
print(f"átlaga:{paros_osszeg/paros_darab:.3f}")
#B.1

darab=0
for szam in lista:
    darab+=1
print(f"{darab}")
print(f"{len (lista)}")
#B.2
print(f"darab:{paros_darab}")

#a2 és b2
parosok_lista=[szam for szam in lista if szam % 2==0]
print(f"A2.számok átlaga: {sum(parosok_lista)/len(parosok_lista):.2f}")
print(f"B2.számok darab: {len(parosok_lista)}")
#AB.3
for szam in lista:
    print(szam,"*"*szam)
    