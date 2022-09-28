# name of student: Bardia
# number of student: 99074122
# purpose of program: Wissel geld berekenen en geven
# function of program: Het berekend wisselgeld en het laat zien hoeveel je van een bepaalde munt hebt gegeven
# structure of program: Er is gebruik gemaakt van if's while loops, inputs, variable's en exeptions.



vijfEuro = 500
drieEuro = 300
tweeEuro = 200
vijftigCent = 50
twintigCent = 20
tienCent = 10
vijfCent = 5
tweeCent = 2
eenCent = 1


toPay = int(float(input('Amount to pay: '))* 100) # Bedrag dat betaald moet worden.
paid = int(float(input('Paid amount: ')) * 100) # Bedrag dat betaald is.
change = paid - toPay # De wisselgeld variable.

if change > 0: # Als de wisselgeld meer dan 0 is begint de programma.
  coinValue = 500 # begin value van een coin
  
  while change > 0 and coinValue > 0: # start van de loop loop stopt pas als alle wissel geld is gegeven
    nrCoins = change // coinValue # berekening change gedeeld door de coinvalue dan krijg je nrCoins
    

    if nrCoins > 0: # als er nog coin gegeven moet worden start de IF
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #hier laat je zien hoeveel je munten van een coinvalue kan geven.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Hier vraagt die hoeveel coins je wilt geven
      change -= nrCoinsReturned * coinValue #Change is - De aantal coins dat ingevoerd is keer de coinvalue

      




# comment on code below: Hier gaat die langs alle coinvalue's
    if coinValue == vijfEuro:
      kaas = nrCoinsReturned
      coinValue = drieEuro
    elif coinValue == drieEuro:
      kaas2 = nrCoinsReturned
      coinValue = tweeEuro
    elif coinValue == tweeEuro:
      kaas3 = nrCoinsReturned
      coinValue = vijftigCent
    elif coinValue == vijftigCent:
      kaas4 = nrCoinsReturned
      coinValue = twintigCent
    elif coinValue == twintigCent:
      kaas5 = nrCoinsReturned
      coinValue = tienCent
    elif coinValue == tienCent:
      kaas6 = nrCoinsReturned
      coinValue = vijfCent
    elif coinValue == vijfCent:
      kaas7 = nrCoinsReturned
      coinValue = tweeCent
    elif coinValue == tweeCent:
      kaas8 = nrCoinsReturned
      coinValue = eenCent
    else:
      coinValue = 0


try:
  if change > 0: # Hier laat hij de change zien dat is ingevuld + als de change niet is compleet terug gegeven
      print('Change not returned: ', str(change) + ' cents')
  else:
      print(f"{vijfEuro}: {kaas}")
      print(f"{drieEuro}: {kaas2}")
      print(f"{tweeEuro}: {kaas3}")
      print(f"{vijftigCent}: {kaas4}")
      print(f"{twintigCent}: {kaas5}")
      print(f"{tienCent}: {kaas6}")
      print(f"{vijfCent}: {kaas7}")
      print(f"{tweeCent}: {kaas8}")
except NameError:
  exit()





