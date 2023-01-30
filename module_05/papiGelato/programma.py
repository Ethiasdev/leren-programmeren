from functions import *
print(WELKOM)

while BESTELLEN == False:
    ijsje = {}
    ijsje['grootte'] = vraag_aantal_bolletje()
    ijsje['smaken'] = vraag_smaak_bolletje(ijsje['grootte'])
    ijsje['verpakking'] = get_hoorntje_of_bakje(ijsje['grootte'])
    ijsje['toppings'] = vraag_toppings()
    ijsje['prijs'] = bereken_prijs(ijsje)
    bestellingen = bestellingen_toevoegen(ijsje)
    nog_een_bestelling = vraag_nog_een_bestellen()
    BESTELLEN = check_nog_bestellen(nog_een_bestelling)

toon_bonnetje(bestellingen)



