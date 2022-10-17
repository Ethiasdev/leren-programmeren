import random
kleurLijst = ["rood", "blauw", "groen", "geel", "bruin"]

hoeveel = int(input("Hoeveel M&M's moeten er gevoegd worden: "))
bag = {

}
getal = 1
for k in range(hoeveel):
    kleur = random.choice(kleurLijst)
    if kleur not in bag:
        
        bag.update({kleur: getal})

    elif kleur in bag:
       
        bag[kleur] += 1
        
        
        
print(bag) 
