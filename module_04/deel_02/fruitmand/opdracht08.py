from fruitmand1 import fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2310,
    'color' : 'green',
    'round' : True
})

gewicht = [fruit['weight'] for fruit in fruitmand if 'weight' in fruit]
totaal = sum(gewicht)
print(totaal)