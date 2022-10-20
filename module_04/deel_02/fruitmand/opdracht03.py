from fruitmand import fruitmand
fruiten = [i['name'] for i in fruitmand if 'name' in i]

for i in fruiten:
    print(i)

