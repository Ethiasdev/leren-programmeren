crossaintjes = int(input("vul hier de aantal crossaintjes: "))

prijsProduct = int(input("vul hier de prijs van het product in centen: ")) 

stokbroden = int(input("vul hier de aantal stokbroden: ")) 

prijsProduct1 = int(input("vul hier de prijs van het product in centen: ")) 

kortingsBonnen = int(input("vul hier de aantal kortingsbonnen: ")) 

kortingsPrijs = int(input("vul hier de prijs van de kortingsbonnen in centen: ")) 

prijs = (crossaintjes * prijsProduct / 100 + stokbroden * prijsProduct1 / 100 - kortingsBonnen * kortingsPrijs / 100)

print ("De feestlunch kost je bij de bakker", prijs, "euro voor de" ' '+ str(crossaintjes) +' ' "croissantjes en de" ' '+ str(stokbroden) +' ' "stokbroden als de" ' '+ str(kortingsBonnen) +' ' "kortingsbonnen nog geldig zijn!")