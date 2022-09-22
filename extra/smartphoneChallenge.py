telefoon1 = "Iphone 13"
telefoon2 = "Samsung Galaxy S22"
telefoon3 = "Asus Zenfone 9"

iphonePrijs = int(input(f"Hoeveel kost de {telefoon1}?:"))
samsungPrijs = int(input(f"Hoeveel kost de {telefoon2}?:"))
asusPrijs = int(input(f"Hoeveel kost de {telefoon3}?:"))

if iphonePrijs > samsungPrijs and asusPrijs:
    print(f"De {telefoon1} is het duurst, de telefoon kost: {iphonePrijs} Euro")
elif samsungPrijs > iphonePrijs and asusPrijs:
    print(f"De {telefoon2} is het duurst, de telefoon kost: {samsungPrijs} Euro")
elif asusPrijs > iphonePrijs and samsungPrijs:
    print(f"De {telefoon3} is het duurst, de telefoon kost: {asusPrijs} Euro")

if iphonePrijs < samsungPrijs and asusPrijs:
    print(f"De {telefoon1} is het goedkoopst, de telefoon kost: {samsungPrijs} Euro")
elif samsungPrijs < iphonePrijs and asusPrijs:
    print(f"De {telefoon2} is het goedkoopst, de telefoon kost: {iphonePrijs} Euro")
elif asusPrijs < iphonePrijs and samsungPrijs:
    print(f"De {telefoon3} is het goedkoopst, de telefoon kost: {asusPrijs} Euro")

if iphonePrijs > 


if iphonePrijs == samsungPrijs:
    print(f"De {telefoon1} en de {telefoon2} zijn even duur de telefoons kosten: {iphonePrijs or samsungPrijs} Euro")

if iphonePrijs > 899 and samsungPrijs > 899:
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
    exit()

if samsungPrijs > iphonePrijs:
    print(f"Het advies is dus de {telefoon1} te kopen. Deze is namelijk {samsungPrijs - iphonePrijs} euro goedkoper dan de {telefoon2}.")

if iphonePrijs > samsungPrijs and 51 > iphonePrijs - samsungPrijs:
    print(f"Het advies is dus de {telefoon1} te kopen. Deze is namelijk {iphonePrijs - samsungPrijs} euro duurder dan de {telefoon2}.")
elif iphonePrijs > samsungPrijs:
    print(f"Het advies is dus de {telefoon2} te kopen. Deze is namelijk {iphonePrijs - samsungPrijs} euro goedkoper dan de {telefoon1}.")

if iphonePrijs == samsungPrijs:
    print(f"Het advies is dus de {telefoon1} te kopen. Deze is namelijk even duur als de {telefoon2} ze kosten allebei {iphonePrijs or samsungPrijs} euro.")




