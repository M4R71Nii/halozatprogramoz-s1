def beker(alakzat, oldal):
    """Bekéri az 'alakzat' 'oldal' oldalának hosszát"""
    oldalhossz =int(input(f"Kérem a {alakzat} {oldal} oldalának hosszát [cm]: "))
    return oldalhossz
def teglalapKerulet(a, b):
    """ kiszamolja az 'a' és 'b' oldal ismeretében a téglalap kerületét. K=2*(a+b)"""
    kerulet = 2* (a+b)
def kiir(alakzat,kerulet):
    
mit = input("[T]églalap vagy [N]égyzet kerületét számoljam ?")
if mit.upper() == "N":
    alap= beker("négyzet","a")
    kerulet = teglalapKerulet(alap,alap)
    print(f"A négyzet kerülete: {kerulet} cm")
elif mit.upper() == "T":
    a_oldal= beker("téglalap","a")
    b_oldal= beker("téglalap","b")
    b_oldal = int(input("Kérem a téglalap b oldalának hosszát[cm]:"))
    kerulet = teglalapKerulet(a_oldal,b_oldal)
    print(f"A téglalap kerülete: {kerulet} cm")
    

    
