from functions import *
ijsje = {}
print(WELKOM)

BESTELLEN = check_zakelijk(vraag_zakelijk())
ijsje['grootte'] = vraag_aantal_bolletje()
ijsje['smaken'] = vraag_smaak_bolletje(ijsje['grootte'])
ijsje['prijs'] = bereken_prijs_liters(ijsje)
bestellingen = bestellingen_toevoegen(ijsje)

while BESTELLEN == False:
    ijsje['grootte'] = vraag_aantal_bolletje()
    ijsje['smaken'] = vraag_smaak_bolletje(ijsje['grootte'])
    ijsje['verpakking'] = get_hoorntje_of_bakje(ijsje['grootte'])
    ijsje['toppings'] = vraag_toppings()
    ijsje['prijs'] = bereken_prijs(ijsje)
    bestellingen = bestellingen_toevoegen(ijsje)
    nog_een_bestelling = vraag_nog_een_bestellen()
    BESTELLEN = check_nog_bestellen(nog_een_bestelling)

toon_bonnetje(bestellingen)



