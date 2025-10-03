# spec_betuk = ["Cs", "Dz","Dzs", "Gy", "Ly", "Ny", "Sz", "Ty", "Zs"]
# nev = input("Add meg a teljes neved: ")
# szavak = nev.strip().split()

# monogram = ""

# for szo in szavak:
#     if len(szo) >= 2 and szo[0].upper() + szo[1].lower() in spec_betuk:
#         monogram += szo[0].upper() + szo[1].lower()
#     else:
#         monogram += szo[0].upper()
# print("A monogramod:", monogram)
# Speciális magyar betűk listája
# spec_betuk = ["Dzs", "Cs", "Dz", "Gy", "Ly", "Ny", "Sz", "Ty", "Zs"]

# nev = input("Add meg a teljes neved: ")

# szavak = nev.strip().split()

# monogram = ""

# for szo in szavak:
#     if len(szo) >= 3 and (szo[0].upper() + szo[1].lower() + szo[2].lower()) in spec_betuk:
#         monogram += szo[0].upper() + szo[1].lower() + szo[2].lower()
#     elif len(szo) >= 2 and (szo[0].upper() + szo[1].lower()) in spec_betuk:
#         monogram += szo[0].upper() + szo[1].lower()
#     else:
#         monogram += szo[0].upper()
# print("A monogramod:", monogram)
# Bekérjük a nevet
nev = input("Add meg a teljes neved: ")
szavak = nev.strip().split()
monogram = ""
for szo in szavak:
    hossz = len(szo)
    betu = szo[0].upper()
    if hossz >= 3:
        a, b, c = szo[0], szo[1], szo[2]
        if (a in "Dd" and b in "Zz" and c in "Ss"):
            betu = a.upper() + b.lower() + c.lower()
    if hossz >= 2 and betu == szo[0].upper():
        a, b = szo[0], szo[1]
        if (
            (a in "Cc" and b in "Ss") or
            (a in "Dd" and b in "Zz") or
            (a in "Gg" and b in "Yy") or
            (a in "Ll" and b in "Yy") or
            (a in "Nn" and b in "Yy") or
            (a in "Ss" and b in "Zz") or
            (a in "Tt" and b in "Yy") or
            (a in "Zz" and b in "Ss")
        ):
            betu = a.upper() + b.lower()
    monogram += betu
print("A monogramod:", monogram)

