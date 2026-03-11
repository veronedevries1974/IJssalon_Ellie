import csv
from helper import *
from presentatie import *

dict_inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750    
}

totaal_inkomsten = som(dict_inkomsten)

presenteer(dict_inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=':')
    for key, value in dict_inkomsten.items():
        writer.writerow([key, value])
          

