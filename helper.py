def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "?"
    return f"het bedrag per persoon is {bedrag_pp} euro."

b = int(input ("welk bedrag zit er in de fooienpot?"))
p = int(input ("over hoeveel mensen moet de pot verdeeld worden?"))

print(fooi_pp(b,p))