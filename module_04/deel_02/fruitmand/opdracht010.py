from fruitmand import fruitmand
naam = [i['name'] for i in fruitmand if 'name' in i]
gewicht = [i['weight'] for i in fruitmand if 'weight' in i]

naamGewicht = {}

for i in range(0,len(naam)):
    naamGewicht[naam[i]] = gewicht[i]

print(naamGewicht)

sort_orders = sorted(naamGewicht.items(), key=lambda x: x[1])
for i in reversed(sort_orders):

	print(i[0], i[1] / 1000, "kg")





