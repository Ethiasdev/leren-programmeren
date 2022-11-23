def nameNAge():
    namen = []
    leeftijd = []

    while True:
        vraagNaam = input("Wat is je naam? type stop als je klaar bent.")
        if vraagNaam == "stop":
            break
        vraagLeeftijd = input("Wat is je leeftijd? type stop als je klaar bent.")
        if vraagLeeftijd== "stop":
            break
        namen.append(vraagNaam)
        leeftijd.append(vraagLeeftijd)
    x = zip(namen, leeftijd)
    return x


for a,b in nameNAge():
    print(f"{a} is {b} jaar")
    
