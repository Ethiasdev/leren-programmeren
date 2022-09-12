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
print ('Bardia')
print (aantal)
print (omschrijving)
print (stuksprijs)

print (aantal * stuksprijs)
print (aantal * omschrijving)
print (str(aantal) + ' ' + omschrijving) # + ' ' + = (spatie)
print (str(aantal) + ' ' + omschrijving + ' ' + str(stuksprijs)) #met 'str' maak je van een float of een int een string
print (f"{aantal} {omschrijving} {stuksprijs}") #zo print je een format dit is een makkelijker manier

inputLengte = input('geef de stukrpijs:')
lengte = float (inputLengte)  #zo vraag je om een input (float, int en str)

print (type(stuksprijs)) #zo weet je wat voor type je variable is
" ' '+ str(crossaintjes) +' ' " #zo maak je een een int/float naar een string in een zin.
a = input('|  Naam      :')
print(a) #input string
print (f"small x {aantal}  €{aantal}") #zo print je alles samen met een variable
a = 5
b = 3
if a > b:
    print ('a is groter dan b') #hier laat je zien dat a groter is dan b waardoor de command door gaat

kaas = int(input("Is de kaas geel?"))
if kaas == "ja":
    print ("ja")

def opposite (number):
    antwoord = number * -1
    return antwoord


if print (opposite(7.2) == -7.2):
    print ("Goed Gedaan")

#met if moet alles op dezelfde lijn als je lange code typt
