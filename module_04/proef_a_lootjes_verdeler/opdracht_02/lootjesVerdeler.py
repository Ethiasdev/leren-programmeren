import random
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
    while True:
        random.shuffle(lijst1)
        for i in range(len(lijst1)):
            if lijst1[i] != lijst1[i - 1]:
                lijst2.append(lijst1[i - 1])

        if len(lijst2) == len(lijst1):
            break

    for i in range(len(lijst2)):
        print(lijst1[i], "heeft", lijst2[i], "getrokken")





            










    


