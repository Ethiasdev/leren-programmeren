WELKOM = "Welkom bij Papi Gelato!"
IJSJE_VRAAG = "Hoeveel bolletjes wilt u?"
LITER_VRAAG = "Hoeveel liter wilt u?"
PRIJS_BOLLETJES = {
    "vanille" : 0.95
}
SMAKEN = ['aardbei', 'chocolade', "vanille"]
TOPPINGS = ["hagelslag", "nootjes"]
PRIJS_HOORNTJES = {
    "hoorntje" : 1.25, "bakje" : 0.75
}
PRIJS_TOPPINGS = {
    "hagelslag": 0.50, "nootjes": 1.00
    }

nogBestellen = False
BESTELLINGEN = []

SOORT_KLANT = ['particulier', 'zakelijk']
KLANT_ZAKELIJK = False
PRIJS_PER_LITER = {
    "vanille" : 9.80
}
BTW = 6

# vraag en geef aantal bolletjes van het ijsje
def vraag_aantal_bolletje(zakelijk: bool) -> int:
    if zakelijk:
        print(LITER_VRAAG)
    else:
        print(IJSJE_VRAAG)
    while True:
        antwoord = int(input("aantal :"))
        if antwoord > 0:
            return antwoord
        print("Kies een getal groter dan 0")



# bereken bakje of hoorntje en vraag dit eventueel.
def get_hoorntje_of_bakje(grootte: int, zakelijk: bool) -> str:
    if zakelijk:
        pass
    else:
        if grootte > 3:
            print("U krijg een bakje")
            return "bakje"
        return input("Wilt u een hoorntje of een bakje:")


def vraag_smaak_bolletje(aantalBolletjes, zakelijk) -> str:
    smaken = []
    for i in range(aantalBolletjes):
        if zakelijk:
            smaak = input(f"Welke smaak wilt u voor liter nummer {i+1}? Aardbei, Chocolade of Vanille? ").lower()
        else:
            smaak = input(f"Welke smaak wilt u voor bolletje nummer {i+1}? Aardbei, Chocolade of Vanille? ").lower()
        if smaak in SMAKEN:
            smaken.append(smaak.upper())
        else:
            print("Sorry dat is geen optie die we aanbieden...")
            i -= 1
    return smaken

    
def vraag_toppings(zakelijk) -> list:
    if zakelijk == True:
        pass
    else:
        print(f"Beschikbare toppings: {TOPPINGS[0]}, {TOPPINGS[1]}.")
        toppings = input("Welke toppings wilt u?: ")
        if toppings in toppings:
            return toppings.split(',')
        else:
            print("Sorry dat is geen optie die we aanbieden...")
            vraag_toppings()

def bestellingen_toevoegen(ijsje: dict) -> list:
    BESTELLINGEN.append(ijsje)
    return BESTELLINGEN

def check_nog_bestellen(nogBestellen: str, zakelijk) -> bool:
    if zakelijk == True:
        return True
    else:
        if nogBestellen == 'ja':
            return False
        else:
            return True

    
def vraag_nog_een_bestellen(zakelijk) -> str:
    if zakelijk == False:
        return input("Wilt u nog een bestelling plaatsen? (ja/nee)")
    else:
        pass

# bereken de prijs van het ijsje
def bereken_prijs(ijsje: dict) -> float:
    prijs = 0.0
    prijs += ijsje["grootte"] * PRIJS_BOLLETJES['vanille']
    if ijsje["verpakking"] == "hoorntje":
        prijs += PRIJS_HOORNTJES["hoorntje"]
    else:
        prijs += PRIJS_HOORNTJES["bakje"]
    return prijs


# toon het bonnetje
def toon_bonnetje(ijsjes: list, zakelijk: bool):
    totaal_prijs = 0.0
    return_string = "Bonnetje: \n" 
    if zakelijk == False:
        for ijsje in ijsjes:
            smaken = ', '.join(ijsje['smaken'])
            toppings = ', '.join(ijsje['toppings'])
            prijs = ijsje['grootte'] * PRIJS_BOLLETJES['vanille'] + sum(PRIJS_TOPPINGS[topping] for topping in ijsje['toppings'])
            prijs += PRIJS_HOORNTJES[ijsje['verpakking']]
            totaal_prijs += prijs
            return_string += f"{smaken}   {ijsje['grootte']} x €{PRIJS_BOLLETJES['vanille']} = €{ijsje['grootte'] * PRIJS_BOLLETJES['vanille']}\n{ijsje['verpakking']}    1 x €{ijsje['verpakking']} = €{PRIJS_HOORNTJES[ijsje['verpakking']]}\nTopping   1 x {toppings} = €{PRIJS_TOPPINGS[toppings]}\n---------------------------\n"                                             

    else:
        for ijsje in ijsjes:
            smaken = ', '.join(ijsje['smaken'])
            totaal_prijs += ijsje['prijs']
            return_string += f"L.{smaken}    {ijsje['grootte']} x €{PRIJS_PER_LITER['vanille']} = €{ijsje['grootte'] * PRIJS_PER_LITER['vanille']}\n"
        
        return_string += f"BTW: €{round(totaal_prijs / 100 * BTW, 2)}\n"
    return_string += f"Totaal : €{round(totaal_prijs,2)}"

    return return_string


def vraag_zakelijk():
    return input("bent u een zakelijk of een particulier klant?: ")


def check_zakelijk(klant):
    return klant == 'zakelijk'


def bereken_prijs_liters(ijsje):
    prijs = 0.0
    prijs += ijsje["grootte"] * PRIJS_PER_LITER['vanille']
    return prijs






