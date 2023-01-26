WELKOM = "Welkom bij Papi Gelato!"
IJSJE_VRAAG = "Hoeveel bolletjes wilt u?"
PRIJS_BOLLETJES = {
    "vanille" : 1.10
}
PRIJS_HOORNTJES = {"hoorntje" : 1.25, "bakje" : 0.75
}
PRIJS_TOPPINGS = {"hagelslag": 0.50, "nootjes": 1.00}

def get_getal():
    pass

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
        return get_getal()
    return input("Wilt u een hoortje of een bakje:")

# bereken de prijs van het ijsje
def bereken_prijs(ijsje: dict) -> float:
    prijs = 0.0
    prijs += ijsje["grootte"] * PRIJS_BOLLETJES['vanille']
    if ijsje["verpakking"] == "hoorntje":
        prijs += PRIJS_HOORNTJES["hoorntje"]
    else:
        prijs += PRIJS_HOORNTJES["bakje"]
    if 'toppings' in ijsje:
        for topping in ijsje['toppings']:
            prijs += PRIJS_TOPPINGS[topping]
    return prijs

# geef de string van het ijsje
def get_ijsje_string(ijsje: dict) -> str:
    smaken = ', '.join(ijsje['smaken'])
    zin = f"{ijsje['verpakking']} met {ijsje['grootte']} bolletjes van smaken {smaken}"
    return zin


# toon het bonnetje
def toon_bonnetje(ijsje: dict):
    print("bolletjes" + str(ijsje["grootte"] * PRIJS_BOLLETJES["vanille"]))
    if 'toppings' in ijsje:
        for topping in ijsje['toppings']:
            print(f"{topping}: {PRIJS_TOPPINGS[topping]}")
    print("totaal " + str(bereken_prijs(ijsje)))

def vraag_smaak_bolletje(bolletje_nummer: int) -> str:
    while True:
        smaak = input(f"Welke smaak wilt u voor bolletje nummer {bolletje_nummer}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
        if smaak in ["A", "C", "M", "V"]:
            return smaak

def vraag_toppings() -> list:
    print("Beschikbare toppings: hagelslag, nootjes.")
    toppings = input("Welke toppings wilt u? (scheid met komma's)")
    return toppings.split(',')

