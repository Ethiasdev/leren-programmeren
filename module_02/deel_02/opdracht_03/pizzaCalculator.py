# Bardia Hatamnejadian
# Opdracht: PizzaCalculator
import sys

smallAmount = 5 #enkel prijs small
mediumAmount = 7 #enkel prijs medium
largeAmount = 12 #enkel prijs large

btw = 9 #btw prijs

try:
 small = int(input("Hoeveel small pizza's wilt u?:"))
except: exit(print("Vul gehele getallen in!"))
try:
 medium = int(input("Hoeveel medium pizza's wilt u?:"))
except: exit(print("Vul gehele getallen in!"))
try:
 large = int(input("Hoeveel large pizza's wilt u?:"))
except: exit(print("Vul gehele getallen in!"))

smallPrice = int(small * smallAmount) #berekening aantal pizza's x enkel prijs
mediumPrice = int(medium * mediumAmount)
largePrice = int(large * largeAmount)


prijs = smallPrice + mediumPrice + largePrice #berekening subtotaal prijs
print ("-----------------------------------------")
print ("|        Bardia's Amazing Pizza's       |")
print ("-----------------------------------------")
print (f"{small}  Small pizza  €{smallAmount}  €{smallPrice} ")
print (f"{medium}  Medium pizza €{mediumAmount}  €{mediumPrice}") 
print (f"{large}  Large pizza  €{largeAmount} €{largePrice} ")
print ("-----------------------------------------")
print (f"Subtotaal:  €{prijs}")
print (f"BTW:        €{prijs / 100 * btw}\n") #berekening BTW
print (f"Totaal:     €{prijs / 100 * btw + prijs}") #berekening totaal prijs incl BTW
print (f"Te betalen: €{prijs / 100 * btw + prijs}")
print ("-----------------------------------------")
print ("Bedankt voor uw bezoek!")
print ("         XXXX          ")



