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
    
   