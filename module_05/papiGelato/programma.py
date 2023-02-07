from functions import *
ijsje = {}
print(WELKOM)



zakelijk = check_zakelijk(vraag_zakelijk())
while nogBestellen == False:
    ijsje['grootte'] = vraag_aantal_bolletje(zakelijk)
    ijsje['smaken'] = vraag_smaak_bolletje(ijsje['grootte'], zakelijk)
    ijsje['verpakking'] = get_hoorntje_of_bakje(ijsje['grootte'], zakelijk)
    ijsje['toppings'] = vraag_toppings(zakelijk)
    ijsje['prijs'] = bereken_prijs(ijsje)
    bestellingen = bestellingen_toevoegen(ijsje)
    nog_een_bestelling = vraag_nog_een_bestellen(zakelijk)
    nogBestellen = check_nog_bestellen(nog_een_bestelling, zakelijk)

print(toon_bonnetje(bestellingen, zakelijk))



