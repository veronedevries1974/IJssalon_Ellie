import math

def mijn_functie_1(a=2, b=4, c=10, d=12):
    return a**2, b**2, c**2, d**2
totaal = mijn_functie_1()
print(totaal)


def mijn_functie_2(getallen_lijst):
    resultaten = []
    for getal in getallen_lijst:
        geheel, decimaal = str(getal).split('.')
        a, b = int(geheel), int(decimaal)
        berekeningen = (f"[{a + b}, {a - b}, {a * b}, {a / b}]")
        resultaten.append(str(berekeningen))
        
    return resultaten

print(mijn_functie_2([12.3, 12.2, 10.5, 100.20]))


#Na lang zoeken en denken kwam ik tot bovenstaande functie 2. De berekening van 100.20 gaat nog niet goed. 
 
        

 