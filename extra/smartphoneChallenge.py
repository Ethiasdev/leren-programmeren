telefoon1 = "Iphone 13"
telefoon2 = "Samsung Galaxy S22"
telefoon3 = "Asus Zenfone 9"

iphonePrijs = int(input(f"Hoeveel kost de {telefoon1}?:"))
samsungPrijs = int(input(f"Hoeveel kost de {telefoon2}?:"))
asusPrijs = int(input(f"Hoeveel kost de {telefoon3}?:"))

if iphonePrijs > samsungPrijs and iphonePrijs > asusPrijs:
    print(f"De {telefoon1} is het duurst, de telefoon kost: {iphonePrijs} Euro")
elif samsungPrijs > iphonePrijs and samsungPrijs > asusPrijs:
    print(f"De {telefoon2} is het duurst, de telefoon kost: {samsungPrijs} Euro")
elif asusPrijs > iphonePrijs and asusPrijs > samsungPrijs:
    print(f"De {telefoon3} is het duurst, de telefoon kost: {asusPrijs} Euro")

if iphonePrijs < samsungPrijs and iphonePrijs < asusPrijs:
    print(f"De {telefoon1} is het goedkoopst, de telefoon kost: {iphonePrijs} Euro")
elif  samsungPrijs < iphonePrijs and samsungPrijs < asusPrijs:
    print(f"De {telefoon2} is het goedkoopst, de telefoon kost: {samsungPrijs} Euro")
elif asusPrijs < iphonePrijs and asusPrijs < samsungPrijs:
    print(f"De {telefoon3} is het goedkoopst, de telefoon kost: {asusPrijs} Euro")

if (iphonePrijs > samsungPrijs or iphonePrijs > asusPrijs) and (iphonePrijs < samsungPrijs or iphonePrijs < asusPrijs):
    print(f"De {telefoon1} zit er tussenin met: {iphonePrijs} Euro")
elif (samsungPrijs > iphonePrijs or samsungPrijs > asusPrijs) and (samsungPrijs < iphonePrijs or samsungPrijs < asusPrijs):
    print(f"De {telefoon2} zit er tussenin {samsungPrijs} Euro")
elif (asusPrijs > samsungPrijs or asusPrijs > iphonePrijs) and (asusPrijs < samsungPrijs or asusPrijs < iphonePrijs):
    print(f"De {telefoon3} zit er tussenin {asusPrijs} Euro")


if iphonePrijs == samsungPrijs == asusPrijs:
    print(f"De {telefoon1}, {telefoon2} en de {telefoon3} zijn even duur de telefoons kosten: {iphonePrijs or samsungPrijs or asusPrijs} Euro")

if iphonePrijs > 899 and samsungPrijs > 899 and asusPrijs > 899:
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
    exit()

if samsungPrijs > iphonePrijs and asusPrijs > iphonePrijs:
    print(f"Het advies is dus de {telefoon1} te kopen. Deze is namelijk {samsungPrijs - iphonePrijs} euro goedkoper dan de {telefoon2} en {asusPrijs - iphonePrijs} goedkoper dan de {telefoon3}.")

if (asusPrijs < samsungPrijs) and (asusPrijs < iphonePrijs) and (asusPrijs - samsungPrijs <= 100) and (asusPrijs - iphonePrijs <= 100):
    print(f"Het advies is dus de {telefoon3} te kopen. Deze is namelijk {iphonePrijs - asusPrijs} euro goedkoper dan de {telefoon1} en {samsungPrijs - asusPrijs} goedkoper dan de {telefoon2}.")
elif (iphonePrijs > samsungPrijs) and (iphonePrijs - samsungPrijs <= 50) and (iphonePrijs - asusPrijs <= 50):
    print(f"Het advies is dus de {telefoon1} te kopen. Deze is namelijk {iphonePrijs - samsungPrijs} euro duurder dan de {telefoon2} en {iphonePrijs - asusPrijs} duurder dan de {telefoon3}.")
elif iphonePrijs > samsungPrijs and asusPrijs > samsungPrijs:
    print(f"Het advies is dus de {telefoon2} te kopen. Deze is namelijk {iphonePrijs - samsungPrijs} euro goedkoper dan de {telefoon1} en {asusPrijs - samsungPrijs} goedkoper dan de {telefoon3}.")

if iphonePrijs == samsungPrijs == asusPrijs:
    print(f"Het advies is dus de {telefoon1} te kopen. Deze is namelijk even duur als de {telefoon2} en de {telefoon3} ze kosten alle 3 {iphonePrijs or samsungPrijs or asusPrijs} euro.")




