import flagpy as fp

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
fp.display('Ivory Coast')
vraag1 =  input ("Vraag 1: Noem de president van dit land!:").lower() # antwoord : Alassane Ouattara

fp.display('Belgium')
vraag2 = input ("Vraag 2: Wat is de hoofdstad van dit land?:").lower() # antwoord : Brussel
if vraag2 != "brussel":
     print ("Hoe weet je dit niet? Je kan beter stoppen!")
     print("++++++++++++++++++++++++++++++++++++++++++++++++")
     print("+ End of The Flag Game                         +")
     print("++++++++++++++++++++++++++++++++++++++++++++++++")
     exit()

fp.display('Egypt')
vraag3 = input ("Vraag 3: In welke continent ligt dit land?:").lower() # antwoord : Afrika
if vraag3 != "afrika":
     print ("Hoe weet je dit niet? Je kan beter stoppen!")
     print("++++++++++++++++++++++++++++++++++++++++++++++++")
     print("+ End of The Flag Game                         +")
     print("++++++++++++++++++++++++++++++++++++++++++++++++")
     exit()

fp.display('Iran')
vraag4 = input ("Vraag 4: Van welke land is deze vlag?:").lower() # antwoord : Iran

fp.display('Japan')
vraag5 = input ("Vraag 5: Wie is de keizer van dit land?:").lower() # antwoord : Naruhito

fp.display('Italy')
vraag6 = input ("Vraag 6: Wat is de bekendste gerecht van dit land?:").lower() # antwoord : Pizza

fp.display('Irak')
vraag7 = input ("Vraag 7: Van welke land is deze vlag?:").lower() # antwoord : Iraq

fp.display('China')
vraag8 = input ("Vraag 7: Hoe noem je mensen in dit land?:").lower() # antwoord : Chinezen

fp.display('France')
vraag9 = input ("Vraag 9: Waar staat dit land bekend voor?:").lower() # antwoord : Eiffeltoren

fp.display('Luxembourg')
vraag10 = input ("Vraag 10: Heeft dit land bergen?:").lower() # antwoord : ja

print ("Goed zo! Je hebt de game gecompleet hier komen de resultaten!")

# de correct checker
if vraag1 == "alassane quattara":
    correct1 = int(1)
else:
    correct1 = int(0)

if vraag2 == "brussel":
    correct2 = int(1)
else:
    correct2 = int(0)

if vraag3 == "afrika":
    correct3 = int(1)
else:
    correct3 = int(0)

if vraag4 == "iran":
    correct4 = int(1)
else:
    correct4 = int(0)

if vraag5 == "naruhito":
    correct5 = int(1)
else:
    correct5 = int(0)

if vraag6 == "pizza":
    correct6 = int(1)
else:
    correct6 = int(0)

if vraag7 == "irak":
    correct7 = int(1)
else:
    correct7 = int(0)

if vraag8 == "chinezen":
    correct8 = int(1)
else:
    correct8 = int(0)

if vraag9 == "eiffeltoren":
    correct9 = int(1)
else:
    correct9 = int(0)

if vraag10 == "ja":
    correct10 = int(1)
else:
    correct10 = int(0)

# End game

correct = correct1+correct2+correct3+correct4+correct5+correct6+correct7+correct8+correct9+correct10

if correct == 10:
    print ("Wow! Je hebt alles goed wat een topper!")
else:
    print (f"Je hebt {correct} van de 10 vragen goed dit kan beter!")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ End of The Flag Game                         +")
print("++++++++++++++++++++++++++++++++++++++++++++++++")





