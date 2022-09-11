crossaintjes = int(input("vul hier de aantal crossaintjes: "))

prijsproduct = int(input("vul hier de prijs van het product in centen: ")) 

stokbroden = int(input("vul hier de aantal stokbroden: ")) 

prijsproduct1 = int(input("vul hier de prijs van het product in centen: ")) 

kortingsbonnen = int(input("vul hier de aantal kortingsbonnen: ")) 

kortingsprijs = int(input("vul hier de prijs van de kortingsbonnen in centen: ")) 

prijs = (crossaintjes * prijsproduct / 100 + stokbroden * prijsproduct1 / 100 - kortingsbonnen * kortingsprijs / 100)

print ("De feestlunch kost je bij de bakker", prijs, "euro voor de" ' '+ str(crossaintjes) +' ' "croissantjes en de" ' '+ str(stokbroden) +' ' "stokbroden als de" ' '+ str(kortingsbonnen) +' ' "kortingsbonnen nog geldig zijn!")