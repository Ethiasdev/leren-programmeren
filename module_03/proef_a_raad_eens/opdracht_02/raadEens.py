import random
import sys

pogingen = 0
rondes = 0
score = 0
cijferControle = 0


while rondes < 20:
    num = random.randint(1, 1)
    raden = input("Wil je een getal raden?: ").lower()
    if raden == "ja":
        print(num)
        while pogingen < 10:  # loop van het getal raden stopt na 10 pogingen
            while cijferControle == 0:
                try: # verplicten van cijfers
                    antwoord = int(input("Raad het getal: "))
                    break
                except ValueError:
                    print("Cijfers alleen AUB!")

            if antwoord == num:
                print("Je hebt het goed geraden!")
                score += 1
                break
            else:
                if antwoord >= num: # berekening of antwoord groter is dan het nummer daarmee berekent hij de verschil
                    verschil = antwoord - num
                elif antwoord <= num:
                    verschil = num - antwoord
                if verschil <= 20: # berekent hier of het heel warm is of warm
                    print("Je bent heel warm!")
                elif verschil <= 50 and verschil >= 20:
                    print("Je bent warm!")
            pogingen += 1
                    
    elif raden == "nee":
        print("Oke jammer!")
        print(f"Jou eind score is {score} van de 20 punten!")
        exit()
    print(f"Je hebt {score} punt(en)!")
    rondes += 1

        

print(f"Jou eind score is {score} van de 20 punten!")
    


