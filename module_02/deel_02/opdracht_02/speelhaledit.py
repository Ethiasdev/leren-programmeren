ticketKost = int(input("vul hier de ticket prijs in centen:"))

vrienden = int(input("vul hier de aantal personen in:")) 

prijsVip = int(input("vul hier de prijs van VIP in centen:")) 

perMin = int(input("vul hier de VIP minuten in:")) 

totalMin = int(input("vul hier de totale minuten in:")) 


prijs = ticketKost / 100 * vrienden + totalMin / perMin * prijsVip / 100 * vrienden

print ("Dit geweldige dagje-uit met" ' '+ str(vrienden) +' ' "mensen in de Speelhal met" ' '+ str(totalMin) +' ' "minuten VR kost je maar", prijs, "euro")