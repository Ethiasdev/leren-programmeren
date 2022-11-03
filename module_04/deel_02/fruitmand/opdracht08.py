from fruitmand import fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2310,
    'color' : 'green',
    'round' : True
})

gewicht = [i['weight'] for i in fruitmand if 'weight' in i]
totaal = sum(gewicht)
print(totaal)