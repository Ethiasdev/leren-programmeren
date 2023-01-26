def check_container(container):
    return container.lower() in ["hoorntje", "bakje"]

def check_nog_bestellen(nogBestellen):
    return nogBestellen.lower() in ["ja", "nee"]

def check_aantal_bolletjes(aantal):
    return 1 <= aantal <= 3 or 4 <= aantal <= 8 or aantal > 8

def check_smaak(smaak):
    return smaak.upper() in ["A", "C", "M", "V"]

def check_topping(topping):
    return topping.upper() in ["A", "B", "C", "D"]

def print_bonnetje(aantal_bolletjes, smaken, aantal_hoorntjes, aantal_bakjes, prijs, topping, topping_prijs):
    print("\nPAPI GELATO")
    print("------------")
    print(f"Bolletjes:   {aantal_bolletjes} x €1.10  = €{aantal_bolletjes * 1.1:.2f}")
    print("Smaken:")
    for i in range(aantal_bolletjes):
        print(f"{i+1}e bolletje: {smaken[i]}")
    if topping != "A":
        print(f"Toppings €{topping_prijs:.2f}")
    print(f"Horrentjes:  {aantal_hoorntjes} x €1.25  = €{aantal_hoorntjes * 1.25:.2f}")
    print(f"Bakjes:      {aantal_bakjes} x €0.75  = €{aantal_bakjes * 0.75:.2f}")
    print("                       -------- +")
    print(f"Totaal                 = €{prijs:.2f}")
    print("------------")
    print("Bedankt voor uw bestelling!")

