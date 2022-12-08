groep_a = []


for a in range(1,4):
    groep_a.append({
        "land" : input(f"Geef de {a}e land op in groep A: "),
        "punten" : 0,
        "doelsaldo" : 0
    })

k = 0
t = 1
for i in range(2):
    print(f"wedstrijd {t}: {groep_a[k]['land']} VS {groep_a[t]['land']}")
    thuis = int(input(f"Hoeveel scoort {groep_a[k]['land']}: "))
    uit = int(input(f"Hoeveel scoort {groep_a[t]['land']}: "))
    if groep_a[k]['doelsaldo'] == 0:
        groep_a[k]['doelsaldo'] = thuis - uit
        groep_a[t]['doelsaldo'] = uit - thuis
    else:
        groep_a[k]['doelsaldo'] += thuis - uit
        groep_a[t]['doelsaldo'] += uit - thuis
    
    if thuis > uit:
        groep_a[k]['punten'] = 3
    else:
        groep_a[t]['punten'] = 3
    
    thuis = 0
    uit = 0
    
    k = k + 1
    t = t + 1



print(groep_a)




