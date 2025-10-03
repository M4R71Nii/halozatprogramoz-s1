elso_nev = input("Add meg a vezetékneved: ")
masodik_nev = input("Add meg a keresztneved: ")
nev = elso_nev + " " + masodik_nev
monogram = nev[0]
for i in range(len(nev) - 1):
    if nev[i] == ' ':
        monogram = monogram + nev[i + 1]
print("A monogramod:", monogram.upper())