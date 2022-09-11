ticketkost = int(input("vul hier de ticket prijs in centen:"))

vrienden = int(input("vul hier de aantal personen in:")) 

prijsVIP = int(input("vul hier de prijs van VIP in centen:")) 

permin = int(input("vul hier de VIP minuten in:")) 

Totalmin = int(input("vul hier de totale minuten in:")) 


prijs = ticketkost / 100 * vrienden + Totalmin / permin * prijsVIP / 100 * vrienden

print ("Dit geweldige dagje-uit met" ' '+ str(vrienden) +' ' "mensen in de Speelhal met" ' '+ str(Totalmin) +' ' "minuten VR kost je maar", prijs, "euro")