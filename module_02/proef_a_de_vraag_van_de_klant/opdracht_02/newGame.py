import flagpy as fp
VRAGEN = ["Vraag 1: Noem de president van dit land!: ","Vraag 2: Wat is de hoofdstad van dit land?: ","Vraag 3: In welke continent ligt dit land?: ","Vraag 4: Van welke land is deze vlag?: ","Vraag 5: Wie is de keizer van dit land?: ","Vraag 6: Wat is de bekendste gerecht van dit land?: ","Vraag 7: Van welke land is deze vlag?: ","Vraag 8: Hoe noem je mensen in dit land?: ","Vraag 9: Waar staat dit land bekend voor?: ","Vraag 10: Heeft dit land bergen?: "]
ANTWOORDEN = ["alassane quattara","brussel","afrika","iran","naruhito","pizza","irak","chinezen","eiffeltoren","ja"]
LANDEN = ['Ivory Coast', 'Belgium','Egypt','Iran','Japan','Italy', 'Iraq', 'China', 'France', 'Luxembourg']
aantalGoed = 0
repeat = " "

def vlaggen(landen):
    fp.display(landen)

def vraagEnControleer(vraag: str, antwoord: str) -> bool:
    vraagSteller = input(vraag).lower()
    if vraagSteller == antwoord:

        return True
    else: 
        return False

print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ The Flag Game!                               +")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
naam = input ("Login met uw naam!:")
welkom = input (f"Welkom {naam} bent u klaar voor de Flag game? ja/nee:").lower()
if welkom == "ja":
    print("Top! de eerste vraag komt eraan!")
elif welkom == "nee":
    print (f"Ach, {naam} ik wist al dat je een loser was.")
    exit()

while repeat != "nee":

    for teller, vraag in enumerate(VRAGEN):
        vlaggen(LANDEN[teller])
        if vraagEnControleer(VRAGEN[teller], ANTWOORDEN[teller]) == True:
            aantalGoed += 1


    print ("Goed zo! Je hebt de game voltooid, denkje je dat je de quiz slecht hebt gemaakt?")
    extra = input("Dan heb je de keuze om 1 extra strik vraag te beantwoorden als je dit goed hebt win je gelijk de quiz MAAR als je hem fout hebt is het GAME OVER! (ja of nee?): ").lower()
    if extra == 'ja':
        extraVraag = input("De vader van Jan heeft 3 zonen; Kwik, Kwek en?: ").lower()
        if extraVraag == "jan":
            print("Goedzo je hebt het goed! Gefeliciteerd!!!")
            exit()
        else:
            print("Helaas.. Game over!")
            print("++++++++++++++++++++++++++++++++++++++++++++++++")
            print("+ End of The Flag Game                         +")
            print("++++++++++++++++++++++++++++++++++++++++++++++++")
    
    if aantalGoed == 10:
        print("Je hebt alles goed!")
    else:
        print(f"Je hebt {aantalGoed} van de 10 vragen goed!")

    repeat = input("Wil je nog een keer spelen? (ja of nee?): ").lower()
    aantalGoed = 0

print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ End of The Flag Game                         +")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
    
