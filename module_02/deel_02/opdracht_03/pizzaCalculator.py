# Bardia Hatamnejadian
# Opdracht: PizzaCalculator


a = 5 #enkel prijs small
b = 7 #enkel prijs medium
c = 12 #enkel prijs large

btw = 9 #btw prijs


small = int(input("Hoeveel small pizza's wilt u?:")) 
medium = int(input("Hoeveel medium pizza's wilt u?:"))
large = int(input("Hoeveel large pizza's wilt u?:"))


smallprice = int(small * a) #berekening aantal pizza's x enkel prijs
mediumprice = int(medium * b)
largeprice = int(large * c)


prijs = smallprice + mediumprice + largeprice #berekening subtotaal prijs
print ("-----------------------------------------")
print ("|        Bardia's Amazing Pizza's       |")
print ("-----------------------------------------")
print (f"{small}  Small pizza  €{a}  €{smallprice} ")
print (f"{medium}  Medium pizza €{b}  €{mediumprice}") 
print (f"{large}  Large pizza  €{c} €{largeprice} ")
print ("-----------------------------------------")
print (f"Subtotaal:  €{prijs}")
print (f"BTW:        €{prijs / 100 * btw}\n") #berekening BTW
print (f"Totaal:     €{prijs / 100 * btw + prijs}") #berekening totaal prijs incl BTW
print (f"Te betalen: €{prijs / 100 * btw + prijs}")
print ("-----------------------------------------")
print ("Bedankt voor uw bezoek!")
print ("         XXXX          ")



