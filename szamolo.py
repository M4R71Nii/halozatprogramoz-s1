szamok=[1,1,2,2,4,5,2,1,3]
egyes_db=0
kettes_db=0
harmas_db=0
negyes_db=0
otos_db=0
for szam in szamok:
    if szam==1 :
        egyes_db+=1
    elif szam==2:
        kettes_db+=1
    elif szam==3:
        harmas_db+=1
    elif szam==4:
        negyes_db+=1
    elif szam==5:
        otos_db+=1
print (f"Az-1es szambol ennyi darab van:{egyes_db}")
print (f"Az-2es szambol ennyi darab van:{kettes_db}")
print (f"Az-3es szambol ennyi darab van:{harmas_db}")
print (f"Az-4es szambol ennyi darab van:{negyes_db}")
print (f"Az-5es szambol ennyi darab van:{otos_db}")

for i in range(1,6):
    print(f"{i} böl van {szamok.count(i)}")


darab=[0,0,0,0,0]
for szam in szamok:
    darab[szam-1]+=1
print(darab)

for i in range(len(darab)):
    print(f"{i+1} bol van {darab[i]}")