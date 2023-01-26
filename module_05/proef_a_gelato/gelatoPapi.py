from functions import *

print("Welkom bij Papi Gelato.")

aantal_bolletjes = 0
smaken = []
aantal_hoorntjes = 0
aantal_bakjes = 0
prijs = 0
topping = ""
topping_prijs = 0

while True:
    aantal = input("Hoeveel bolletjes wilt u? ")
    try:
        aantal = int(aantal)
        if check_aantal_bolletjes(aantal):
            if aantal <= 3:
                container = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
                if check_container(container):
                    container = container.lower()
                    aantal_bolletjes += aantal
                    prijs += aantal * 1.1
                    if container == "hoorntje":
                        aantal_hoorntjes += 1
                        prijs += 1 * 1.25
                        topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
                        if check_topping(topping):
                            topping = topping.upper()
                            if topping == "A":
                                topping_prijs = 0
                            elif topping == "B":
                                topping_prijs = 0.5
                            elif topping == "C":
                                topping_prijs = aantal * 0.3
                                prijs += topping_prijs
                            elif topping == "D":
                                topping_prijs = 0.6
                                prijs += topping_prijs
                        else:
                            print("Sorry, dat snap ik niet...")
                            continue
                    elif container == "bakje":
                        aantal_bakjes += 1
                        prijs += aantal * 0.75
                        topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
                        if check_topping(topping):
                            topping = topping.upper()
                            if topping == "A":
                                topping_prijs = 0
                            elif topping == "B":
                                topping_prijs = 0.5
                            elif topping == "C":
                                topping_prijs = aantal * 0.3
                                prijs += topping_prijs
                            elif topping == "D":
                                topping_prijs = 0.9
                                prijs += topping_prijs
                        else:
                            print("Sorry, dat snap ik niet...")
                            continue
                    for i in range(aantal):
                        smaak = input(f"Welke smaak wilt u voor bolletje nummer {i+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
                        if check_smaak(smaak):
                            smaken.append(smaak.upper())
                        else:
                            print("Sorry, dat snap ik niet...")
                            i -= 1
                    print(f"Hier is uw {container} met {aantal} bolletje(s).")
                    nogBestellen = input("Wilt u nog iets bestellen? ")
                    if check_nog_bestellen(nogBestellen):
                        if nogBestellen == "ja":
                            continue
                        elif nogBestellen == "nee":
                            print_bonnetje(aantal_bolletjes, smaken, aantal_hoorntjes, aantal_bakjes, prijs, topping, topping_prijs)
                            break
                else:
                    print("Sorry, dat snap ik niet...")
                    continue
            elif aantal > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
                continue
            else:
                container = "bakje"
                aantal_bolletjes += aantal
                aantal_bakjes += 1
                prijs += aantal * 1.1 + aantal_bakjes * 0.75
                topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
                if check_topping(topping):
                    topping = topping.upper()
                    if topping == "A":
                        topping_prijs = 0
                    elif topping == "B":
                        topping_prijs = 0.5
                    elif topping == "C":
                        topping_prijs = aantal * 0.3
                        prijs += topping_prijs
                    elif topping == "D":
                        topping_prijs = 0.9
                        prijs += topping_prijs
                else:
                    print("Sorry, dat snap ik niet...")
                    continue
                for i in range(aantal):
                    smaak = input(f"Welke smaak wilt u voor bolletje nummer {i+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
                    if check_smaak(smaak):
                        smaken.append(smaak.upper())
                    else:
                        print("Sorry, dat snap ik niet...")
                        i -= 1
                print(f"Hier is uw {container} met {aantal} bolletje(s).")
                nogBestellen = input("Wilt u nog iets bestellen? ")
                if check_nog_bestellen(nogBestellen):
                    if nogBestellen == "ja":
                        continue
                    elif nogBestellen == "nee":
                        print_bonnetje(aantal_bolletjes, smaken, aantal_hoorntjes, aantal_bakjes, prijs, topping, topping_prijs)
                        break
                else:
                    print("Sorry, dat snap ik niet...")
                    continue
        else:
            print("Sorry, dat snap ik niet...")
            continue
    except ValueError:
        print("Sorry, dat snap ik niet...")
        continue
