def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2
#########################################
keuze = " "
while not keuze in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    keuze = input("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?: ").lower()
    if keuze == "niets":
        exit()
#########################################
aantal = -1
while True:
    if aantal > -1 and keuze != 'i':
        number2 = int(input("Geef de 2e getal op: "))
        
    elif not keuze in ('e', 'f', 'g', 'h', 'i'):
        number1 = int(input("Geef een getal op: "))
        number2 = int(input("Geef nog een getal op: "))

    elif not keuze in ('a', 'b', 'c', 'd', 'i'):
        number1 = int(input("Geef een getal op: "))

    else:
        exit()

    #########################################
    if keuze == "a":
        aantal = addition(number1, number2)
        print(aantal)
    elif keuze == "b":
        aantal = subtraction(number1, number2)
        print(aantal)
    elif keuze == "c":
        aantal = multiplication(number1, number2)
        print(aantal)
    elif keuze == "d":
        aantal = division(number1, number2)
        print(aantal)
    elif keuze == "e":
        number2 = 1
        aantal = addition(number1, number2)
        print(aantal)
    elif keuze == "f":
        number2 = 1
        aantal = subtraction(number1, number2)
        print(aantal)
    elif keuze == "g":
        number2 = 2
        aantal = multiplication(number1, number2)
        print(aantal)
    else:
        number2 = 2
        aantal = division(number1, number2)
        print(aantal)

    keuze = input(f"Wil je wat met het antwoord ({aantal}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) Nee?")
    number1 = aantal




    







