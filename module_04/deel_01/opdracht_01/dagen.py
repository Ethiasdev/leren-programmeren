dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")


print("Alle dagen van de week zijn: ")
for k in dagen:
    print(k)

print("Alle werkdagen van de week zijn: ")
for x in dagen[0:5]:
    print(x)

print("De weekenddagen zijn: ")
for j in dagen[5:7]:
    print(j)


print("Alle dagen van de week in omgekeerde volgorde zijn: ")
for z in reversed(dagen):
    print(z)

print("De werkdagen in omgekeerde volgorde zijn: ")
for z in reversed(dagen[0:5]):
    print(z)

print("De weekenddagen in omgekeerde volgorde zijn: ")
for z in reversed(dagen[5:7]):
    print(z)

    


    