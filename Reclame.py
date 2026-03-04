def aanbieding_1(smaak="aardbei", prijs=4, korting=0.1): 
    korting = prijs - (prijs * korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro, voor {korting:.2f} euro."
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

#een float op twee decimalen laten eindigen {bedrag:.2f}

def inkomsten_totaal(inkomsten):
    
    inkomsten = 220 + 430 + 125 + 160 + 205 + 90 + 345
    bedrag = inkomsten * 0.09
    
    resultaten = (f"Het totaal van alle inkomsten deze week is {inkomsten} euro, waarover {bedrag} euro btw betaald dient te worden.")  
    return resultaten

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))
