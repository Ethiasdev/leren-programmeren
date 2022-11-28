import flagpy as fp
def antwoordenChecker() -> int: #Checkt de antwoorden en geeft aan hoeveel er goed zijn.
    correct = 0
    for i in range(len(antwoorden)):
        if correcteAntwoorden[i] == antwoorden[i]:
            correct += 1
    return correct

correcteAntwoorden = ["alassane quattara","brussel","afrika","iran","naruhito","pizza","irak","chinezen","eiffeltoren","ja"]
antwoorden = []


# de login stappen van de game:
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

# de vragen:
repeat = ''
while repeat != 'nee':
    fp.display('Ivory Coast')   
    vraag1 =  input ("Vraag 1: Noem de president van dit land!:").lower() # antwoord : Alassane Ouattara
    antwoorden.append(vraag1)

    fp.display('Belgium')    
    vraag2 = input ("Vraag 2: Wat is de hoofdstad van dit land?:").lower() # antwoord : Brussel
    antwoorden.append(vraag2)
    if vraag2 != "brussel":
        print ("Hoe weet je dit niet? Je kan beter stoppen!")
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+ End of The Flag Game                         +")
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        exit()

    fp.display('Egypt')    
    vraag3 = input ("Vraag 3: In welke continent ligt dit land?:").lower() # antwoord : Afrika
    antwoorden.append(vraag3)
    if vraag3 != "afrika":
        print ("Hoe weet je dit niet? Je kan beter stoppen!")
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+ End of The Flag Game                         +")
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        exit()

    fp.display('Iran')    
    vraag4 = input ("Vraag 4: Van welke land is deze vlag?:").lower() # antwoord : Iran
    antwoorden.append(vraag4)

    fp.display('Japan')    
    vraag5 = input ("Vraag 5: Wie is de keizer van dit land?:").lower() # antwoord : Naruhito
    antwoorden.append(vraag5)

    fp.display('Italy')    
    vraag6 = input ("Vraag 6: Wat is de bekendste gerecht van dit land?:").lower() # antwoord : Pizza
    antwoorden.append(vraag6)

    fp.display('Iraq')    
    vraag7 = input ("Vraag 7: Van welke land is deze vlag?:").lower() # antwoord : Iraq
    antwoorden.append(vraag7)

    fp.display('China')    
    vraag8 = input ("Vraag 8: Hoe noem je mensen in dit land?:").lower() # antwoord : Chinezen
    antwoorden.append(vraag8)

    fp.display('France')    
    vraag9 = input ("Vraag 9: Waar staat dit land bekend voor?:").lower() # antwoord : Eiffeltoren
    antwoorden.append(vraag9)

    fp.display('Luxembourg')    
    vraag10 = input ("Vraag 10: Heeft dit land bergen?:").lower() # antwoord : ja
    antwoorden.append(vraag10)

    print ("Goed zo! Je hebt de game voltooid, Denkje dat je quiz slecht hebt gemaakt?")
    extra = input("Dan heb je de keuze om 1 extra strik vraag te beantwoorden als je dit goed hebt win je gelijk de quiz MAAR als je hem fout hebt is het GAME OVER! (ja of nee?): ").lower()
    if extra == 'ja':
        extraVraag = input("De vader van Jan heeft 3 zonen; Kwik, Kwek en?: ").lower()
        if extraVraag == "jan":
            print("Goedzo je hebt het goed! Gefeliciteerd!!!")
            exit()
        else:
            print("Helaas.. Game over!")


    # de correct checker


    
    if antwoordenChecker() == 10:
        print ("Wow! Je hebt alles goed wat een topper!")
    else:
        print (f"Je hebt {antwoordenChecker()} van de 10 vragen goed dit kan beter!")
    
    repeat = input("Wil je nog een keer spelen? (ja of nee?): ").lower()

print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ End of The Flag Game                         +")
print("++++++++++++++++++++++++++++++++++++++++++++++++")






