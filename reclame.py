def aanbieding_1(smaak = aardbei, prijs = 4, korting = 0.1):
    prijs_na_korting = prijs * korting
    uitvoer = f"vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

def inkomsten_totaal(inkomsten = [220, 430, 125, 160, 205, 90, 345], btw = 21):
totaal = 0
for bedrag in inkomsten:
totaal = bedrag
btw_bedrag = totaal * btw
uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
return totaal

mijn_lijst = 10,5,3,2,1,2,9 

def laag_en_hoog(mijn_lijst):
uitvoer = []
laagste = min(mijn_lijst)
hoogste = max(mijn_lijst)
uitvoer.append(laagste)
uitvoer.append(hoogste)
return uitvoer

def gemiddelde(mijn_lijst):
aantal = len(mijn_lijst)
totaal = 0
for element in mijn_lijst:
totaal += element
gemiddelde = totaal / aantal
return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."