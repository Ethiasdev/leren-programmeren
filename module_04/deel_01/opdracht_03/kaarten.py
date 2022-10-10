import random
types = ["harten", "klaveren", "schoppen", "ruiten"]
bijzonder = ["aas","boer", "vrouw", "heer"]
deck = ["joker", "joker2"]
for k in types:
    for x in bijzonder:
        deck.append(f"{k} {x}")
    for z in range(2,10,1):
        deck.append(f"{k} {z}")
random.shuffle(deck)
for i in range(1,8):
    kaart = random.choice(deck)
    print(f"kaart {i}: {kaart}")
    deck.remove(kaart)
print(f"deck (47 kaarten): {deck}")


