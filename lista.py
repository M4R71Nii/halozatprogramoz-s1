gyumolcsok=["eper","dinnye"]
jegyek=[2,5]
jegyek.append(1)
gyumolcsok.append("alma")
print(jegyek)
print(gyumolcsok)
jegyek.sort()
print(jegyek)
print(sorted(jegyek))
gyumolcsok.remove("dinnye")
print(gyumolcsok)
gyumolcsok.insert(1,"banan")
print(gyumolcsok)
gyumolcsok=[]
jegyek.reverse()
print(jegyek)
print(gyumolcsok.index("banan"))
print(jegyek.count(5))
print(sum(jegyek))
print(min(jegyek))
print(max(jegyek))
print(len(jegyek))
print(f"{', '.join(gyumolcsok)}")
print(f"{', '.join(map(str,jegyek))}")
for jegy in jegyek:
    print(jegy)
for i in range(len(gyumolcsok)):
    print(gyumolcsok[i])
mx=[
    [1,2,3],
    [4,5,6]
]
for sor in mx:
    for oszlop in sor :
        print(oszlop,end=", ")
        print(",".join(map(str,sor)))
    print()
    
    
    
    