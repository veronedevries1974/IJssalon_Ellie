<<<<<<< HEAD
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

reclame_tekst4 = ['VANDAAG', 'IN', 'DE', 'AANBIEDING:', 'VANILLE-IJS', '1 LITER', 'SLECHTS', '€2.40']
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())
=======
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

reclame_tekst4 = ['VANDAAG', 'IN', 'DE', 'AANBIEDING:', 'VANILLE-IJS', '1 LITER', 'SLECHTS', '€2.40']
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())
>>>>>>> 4a0153c50d5ffa484c8a06dd0e07e3f0e6ed9297
