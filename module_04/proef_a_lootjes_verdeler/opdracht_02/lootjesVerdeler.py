import random
import collections
lijst1 = []
lijst2 = []

vraag = input("Wilt u lootjes trekken?: ").lower()
if vraag == "ja":
    while True:
        namen = input("Wat zijn de namen van de spelers? Type (done) wanneer alle namen ingevuld zijn!: ").lower()
        if namen == "done":
            break
        lijst1.append(namen)
else:
    exit()


if len(lijst1) < 3:
    print("Er zijn niet meer dan 3 namen opgenoemd of niet alle namen zijn uniek..")
elif len(lijst1) > len(set(lijst1)):
    print("Er zijn niet meer dan 3 namen opgenoemd of niet alle namen zijn uniek..")
else:
    for k in lijst1:
        if len(set(lijst1)) != len(set(lijst2)):
            picker = random.choice(lijst1)
            lijst2.append(picker)
        else:
            lijst2.remove(picker)

for a,b in zip(lijst1, lijst2):
    print(a,b)
        





            










    


