#ciklusok
lista = [1,2,3,4,5]

def osszegez(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg
print(f"A lista elemeinek összege: {osszegez(lista)}")

def paros_db(lista):
    darab = 0
    for elem in lista:
        if elem % 2 == 0:
            darab += 1
    return darab
print(f"A lista páros elemeinek darabszáma: {paros_db(lista)}")

print("*"*5)

for i in range(5):
    print("*" , end="")
print("")


def rajzolj_piramist(magassag):
    for i in range(1, magassag + 1):
        szokoz = ' ' * (magassag - i)
        csillag = '*' * (2 * i - 1)
        print(szokoz + csillag)


print("adj meg számokat")
osszeg= 0
while True:
    adat = input("Szám: ")
    if adat.strip()== "":
        break
    try:
       
        osszeg += szam
    except ValueError:
        print("ez nem szám ") 

print (f"az összeg eredménye{osszeg}")     
        
        