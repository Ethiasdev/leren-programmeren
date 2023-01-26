from functions import *
print(WELKOM)
ijsje = {}



ijsje['grootte']= vraag_aantal_bolletje()
ijsje['verpakking']= get_hoorntje_of_bakje(ijsje['grootte'])
ijsje['smaken'] = []
for i in range(ijsje['grootte']):
    smaak = vraag_smaak_bolletje(i+1)
    ijsje['smaken'].append(smaak)
    ijsje['prijs'] = bereken_prijs(ijsje)

ijsje['toppings'] = vraag_toppings()
ijsje['prijs'] = bereken_prijs(ijsje)

print("Hier is uw " + get_ijsje_string(ijsje))
toon_bonnetje(ijsje)
