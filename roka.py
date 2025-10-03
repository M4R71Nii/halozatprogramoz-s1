libak = []
with open("libak.txt") as fin:
    for suly in fin:
        libak.append(int(suly.strip()))
print(libak)


roka_kilo = 0

for liba in libak:
    if liba <= 3:
        roka_kilo = roka_kilo + liba
print(roka_kilo)
        
roka_darab = 0

for liba in libak:
    if liba <= 3:
        roka_darab = roka_darab + 1
print(f"Átlag:{round(roka_kilo/roka_darab),2}")




volt_legalabb3 = False 
for liba in libak:
    if liba >= 3:
        volt_legalabb3 = True
        break
if volt_legalabb3:
    print("volt")
else:
    print("nem")
    

index = 0
while not(libak[index] > 3):
    index += 1 
print(f"{index+1}. napon sikerult eloszor 3kg-nal ")

van_6k_s = False
i = 0
while i  < len(libak) and not(libak[i] ==6):
    i += 1

if  i<len(libak):
    print(f"volt 6 kg sulyu liba a {i+1}. napon")
else:
    print(f"volt kg sulyl liba")
    
farkas_liba = 0

for liba in libak:
    if liba < 3:
        farkas_liba = farkas_liba + 1
print(f"{farkas_liba}")

max_index = 0
for index in range(len(libak)):
    if libak[index] > libak[max_index] and libak[index]:
        max_index = index
print(f"{max_index}")

with open("libak_jo.txt","w" encoding="utf8") as fout:
    for liba in libak:

print(liba*1.1, file=fout)


   