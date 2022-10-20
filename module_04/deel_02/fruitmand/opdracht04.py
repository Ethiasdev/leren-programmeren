from fruitmand import fruitmand
import random

aantal = int(input("Hoeveel fruit wilt u?: "))

fruiten = [i['name'] for i in fruitmand if 'name' in i]

fruit = (random.choices(fruiten, k=aantal))

for l in fruit:
    print(l)





