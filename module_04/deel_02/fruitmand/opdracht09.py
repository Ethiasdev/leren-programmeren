from fruitmand import fruitmand
newFruitmand = [

    item for item in fruitmand if item.get('name') != "druif"
]
kleur = [i['color'] for i in newFruitmand if 'color' in i]
lijst = []

for i in kleur:
    if i in lijst:
        continue
    print(i)
    lijst.append(i)
    
    
    