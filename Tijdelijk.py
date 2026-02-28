prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5,
}

a = 3
v = 4 
c = 5
aanbieding = a * 0.8 

reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}")

reclame_tekst2 = reclame_tekst[:62]

reclame_tekst3 = (reclame_tekst2.upper())

print(reclame_tekst3)
  