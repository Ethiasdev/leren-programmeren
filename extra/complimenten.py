import random
aantalComplimenten = int(input("Hoeveel complimenten wil je hebben?: "))
naam = input("Wat is je naam: ")

complimenten = ("Je bent super", "Je ziet er goed uit", "Mooie schoenen", "Mooi haar")
a = ""
x = 0

while x < aantalComplimenten:
    kies = random.choice(complimenten)
    if kies != a:
        print(f"{kies}, {naam}")
        a = kies
        x = x + 1

    

