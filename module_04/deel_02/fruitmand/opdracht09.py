from fruitmand import fruitmand
newFruitmand = [

    item for item in fruitmand if item.get('name') != "druif"
]
kleur = [i['color'] for i in fruitmand if 'color' in i]
for i in kleur: print(i)