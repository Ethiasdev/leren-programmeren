from fruitmand import fruitmand
fruiten = [i['name'] for i in fruitmand if 'name' in i]

for k in reversed(fruiten):
    print(k)