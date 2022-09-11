ticketkost = 7.45
vrienden = 4
prijsVIP = 0.37
permin = 5
Totalmin = 45

prijs = ticketkost * vrienden + Totalmin / permin * prijsVIP * vrienden

print ("Dit geweldige dagje-uit met" ' '+ str(vrienden) +' ' "mensen in de Speelhal met" ' '+ str(Totalmin) +' ' "minuten VR kost je maar", prijs, "euro")