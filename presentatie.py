import csv
from boekhouding import totaal_inkomsten
def presenteer(totaal)
    totaal = totaal_inkomsten
    return totaal

def mijn_dict ()
    print ("aardbei_ijs_totaal" : 1000)
    print("vanille_ijs_totaal" : 2000)
    print("chocolade_ijs_totaal" : 1500) 
    print("waterijsjes_totaal" : 750)
    print("*************************")
    totaal1 = 1000 + 2000 + 1500 + 750
    print(totaal1)

with open('boekhouding.csv’, 'w',newline='') as csvfile:
     for key, value in inkomsten.items():
     writer = csv.writer(csvfile, delimter=';')
     writer.writerow([key,value])