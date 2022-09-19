prijsConsole = 55
prijsPC = 45
korting = 15

game = input ("Bent u een PC of Console gamer?:").lower()

if game == "pc":
    prijs = prijsPC
    print (f"Minecraft kost {prijs} EURO")
elif game == "console":
    prijs = prijsConsole
    if game == "console":
        member = input ("Bent u een Gold member?").lower()
    if member == "ja":
        print (f"Mincraft kost {prijs - korting} EURO")
    else:
        print(f"Minecraft kost {prijs} EURO")