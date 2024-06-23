def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    return "het bedrag per persoon is {bedrag_pp} euro"

def onderstrep(tekst):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst)) * "="
    return uit

from helper import onderstrep

uitvoer = onderstreep("aanbiedingen")
uitvoer.append("aardbeienij, emmertje van 1 liter: 2 euro")
uitvoer.append("slagroom, spuitbus van 1 liter: 2 euro")

print()

for el in uitvoer:
    print el

def som(a,b,c,d)
    totaal = a + b + c + d
    return totaal