grootsteGetal = 0
kleinsteGetal = 1000
delen = ""
for getal in range(10):
    getallen = int(input("Vul hier 10 getallen in: "))
    if getallen > grootsteGetal:
        grootsteGetal = getallen
    if getallen < kleinsteGetal:
        kleinsteGetal = getallen
    if getallen % 3 == 0:
        delen += (f"{getallen}")

print(delen)
print(getallen)
print(kleinsteGetal)
