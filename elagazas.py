import random

gondolt_szam = random.randint(1,3)

#print(f"gonolt szám: {gondolt_szam})
bekert_szam =int(input("kérem a tippet"))

if gondolt_szam == bekert_szam:
    print("Nagyobbra gondoltam!")
elif gondolt_szam > bekert_szam:
    print("Kisebbre gondoltam!")
else:
    print("Kisebbre gondoltam")

#keszits egy fuggvenyt elojel neven, mely átvesz egy egész számot és az elojelet adja vissza 

def elojel(szam):
    if szam >=0:
        return "+"
    else:
        return "-"


szam = int(input("Kérek egy számot elojellel"))

print(f"A {szam} elojele: {elojel(szam)}")

def tesztesetek():
        teszt(5, "+")
        teszt(-3,"-")
        

def teszt(szam , elvart_elojel):
    if elojel(szam) == elvart_elojel:
        print(f"elojel({szam})=={elvart_elojel} true")
    else:
        print(f"elojel({szam})=={elvart_elojel} false")