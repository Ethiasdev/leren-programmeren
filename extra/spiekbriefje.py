# commentaar schrijf je met #


#########################################################################
# variabelen
#########################################################################
#voorbeeld:
aantal = 6 #dit is een integer, integer is een geheel getal (int)
omschrijving = 'Lays naturel 300G' #dit is een string (str)
stuksprijs = 0.89 #dit is een float, float is een getal met een komma


#########################################################################
# built in functies
#########################################################################
input('Wat is uw naam?:')
int(input('Wat is uw naam?:'))
naam = input('Wat is uw naam?:')
small = int(input("Hoeveel small pizza's wilt u?:"))
small = float(input("Hoeveel small pizza's wilt u?:")) #Verschillende soorten inputs!


print (f"De dag is voorbij over {small} uur en {naam} minuten") # format printing!


if small > naam:
    print(f"a is het grootste getal: {small}")
elif small < naam:
    print (f"a is het kleinste getal: {naam}")
else:
    print (f"a en b zijn even groot") #zo gebruik je if's en elif's en else's!


if praktijk > 4 and diploma == "ja" and rijbewijs == "ja" and hoed == "ja" and snor > 10 or krullen > 20 and lengte > 150 and gewicht > 90 and certificaat == "ja" and veter == "ja" and voorhoofd == "ja" and kaas == "ja":
    print ("Proficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV!")
elif praktijk < 4 or diploma == "nee" or rijbewijs == "nee" or hoed == "nee" or snor < 10 or krullen < 20 or lengte < 150 or gewicht < 90 or certificaat == "nee" or veter == "nee" or voorhoofd == "nee" or kaas == "nee":
    print ("U voldoet niet aan onze strenge eisen voor de functie van Circusdirecteur, het spijt ons!") #zo kan je iemand een vragen lijst laten invullen en hiermee elke antwoord checken met and of or!


try:
 small = int(input("Hoeveel small pizza's wilt u?:"))
except: exit(print("Vul gehele getallen in!")) #hiermee kan je met except een melding laten zien wanneer er iets fout word ingevuld of met een error! je kan ook tussen de except een specefieke foutmelding zetten!