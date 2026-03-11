mijn_dict = {
    "vis":10,
    "vlees": 25,
    "overig":15
}    

totaal = 50


def presenteer(mijn_dict, totaal):
    
    for k, v in mijn_dict.items():
        print(f"{k}: {v} euro")
    
    tekst = f"totaal: {totaal} euro"
    lengte = len(tekst)+10
    print(lengte * "=") 
    print(tekst)

presenteer(mijn_dict, totaal)

    


