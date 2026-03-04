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

def laag_en_hoog(mijn_lijst):
    
    mijn_lijst = 220, 430, 125, 160, 205, 90, 345
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    
    resultaten = (f"Laagste waarde is {laag} en hoogste waarde is {hoog}")
    
    return resultaten
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    
    mijn_lijst = 220, 430, 125, 160, 205, 90, 345
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    bedrag = totaal / aantal

    resultaten = (f"De gemiddelde inkomsten deze week zijn {bedrag:.2f} euro")
    
    return resultaten
print(gemiddelde([220, 430, 125, 160, 205, 90, 345])) 
    
def meervoudig(invoer_lijst):
    
    invoer_lijst = 10, 5, 3, 2, 1, 2, 9
    laag = min(invoer_lijst)
    hoog = max(invoer_lijst)
    resultaten = f"Hoogste waarde is {hoog} en laagste waarde is {laag}"
    
    return resultaten

print(meervoudig([10, 5, 3, 2, 1, 2, 9]))
