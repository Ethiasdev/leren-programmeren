lijst = []
aantal = 10
while len(lijst) < aantal:
    getallen = int(input(f"Noem {aantal} getallen op: "))
    lijst.append(getallen)

largeNumber = max(lijst)
lowNumber = min(lijst)

result = list (filter (lambda x: (x % 3 == 0), lijst))

print(f"Dit is de grootste getal: {largeNumber}")
print(f"Dit is de kleinste getal: {lowNumber}")
print(f"Dit zijn de getallen die je kan delen door 3: {*result,}")



