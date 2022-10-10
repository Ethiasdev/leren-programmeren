dagen = ("", "maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")


print("Alle dagen van de week zijn: ")
for k in range (len(dagen)):
    print(dagen[k])


print("De werkdagen zijn: ")
print(dagen[1:6])

print("De weekenddagen zijn: ")
print(dagen[6:8])


print("Alle dagen van de week in omgekeerde volgorde zijn: ")
print(dagen[7:0:-1])

print("De werkdagen in omgekeerde volgorde zijn: ")
print(dagen[5:0:-1])

print("De weekenddagen in omgekeerde volgorde zijn: ")
print(dagen[7:5:-1])
    


    