WELKOM = "Welkom bij Papi Gelato!"
IJSJE_VRAAG = "Hoeveel bolletjes wilt u?"
PRIJS_BOLLETJES = {
    "vanille" : 1.10
}
SMAKEN = ['aardbei', 'chocolade', 'munt', "vanille"]
TOPPINGS = ["hagelslag", "nootjes"]
PRIJS_HOORNTJES = {
    "hoorntje" : 1.25, "bakje" : 0.75
}
PRIJS_TOPPINGS = {
    "hagelslag": 0.50, "nootjes": 1.00
    }

BESTELLEN = False
BESTELLINGEN = []

# vraag en geef aantal bolletjes van het ijsje
def vraag_aantal_bolletje() -> int:
    print(IJSJE_VRAAG)
    while True:
        antwoord = int(input("aantal :"))
        if antwoord > 0:
            return antwoord
        print("Kies een getal groter dan 0")

# bereken bakje of hoorntje en vraag dit eventueel.
def get_hoorntje_of_bakje(grootte: int) -> str:
    if grootte > 3:
        print("U krijg een bakje")
        return "bakje"
    return input("Wilt u een hoortje of een bakje:")


def vraag_smaak_bolletje(aantalBolletjes) -> str:
    smaken = []
    for i in range(aantalBolletjes):
        smaak = input(f"Welke smaak wilt u voor bolletje nummer {i+1}? Aardbei, Chocolade, Munt of Vanille? ").lower()
        if smaak in SMAKEN:
            smaken.append(smaak.upper())
        else:
            print("Sorry, dat snap ik niet...")
            i -= 1
    return smaken

top = ''
for i in TOPPINGS:
    top += TOPPINGS[i]
    
def vraag_toppings() -> list:
    print(f"Beschikbare toppings: {TOPPINGS[0]}, {TOPPINGS[1]}.")
    toppings = input("Welke toppings wilt u? (scheid met komma's)")
    return toppings.split(',')

def bestellingen_toevoegen(ijsje: dict) -> list:
    BESTELLINGEN.append(ijsje)
    return BESTELLINGEN

def check_nog_bestellen(nogBestellen: str) -> bool:
    if nogBestellen == "ja":
        BESTELLEN = False
        return BESTELLEN
    else:
        BESTELLEN = True
        return BESTELLEN

def vraag_nog_een_bestellen() -> str:
    return input("Wilt u nog een bestelling plaatsen? (ja/nee)")


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
def toon_bonnetje(ijsjes: list):
    totaal_prijs = 0.0
    print("Bonnetje:")
    for ijsje in ijsjes:
        smaken = ', '.join(ijsje['smaken'])
        toppings = ', '.join(ijsje['toppings'])
        prijs = ijsje['grootte'] * PRIJS_BOLLETJES['vanille'] + sum(PRIJS_TOPPINGS[topping] for topping in ijsje['toppings'])
        prijs += PRIJS_HOORNTJES[ijsje['verpakking']]
        totaal_prijs += prijs
        print(f"{ijsje['grootte']} bolletjes {smaken} in {ijsje['verpakking']} met toppings {toppings} : €{prijs}")
    print(f"Totaal : €{round(totaal_prijs,2)}")


