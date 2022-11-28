#1
tafel = 1
getal = 1
getal2 = 1
while tafel <= 13:
    print(f"Tafel van {tafel}")
    while getal2 <= 10:
        print(f"{getal} x {getal2} = {getal * getal2}")
        getal2 += 1
    getal2 = 1
    getal += 1
    tafel += 1

#2
lijst = [5, 12, 19, 27, 3]

#3
lijst.append(25)

#4
print(len(lijst))

#5
print(lijst)
lijst.remove(12)
print(lijst)

#6
print(lijst)
lijst.pop(0)
print(lijst)

#7
lijst.insert(0, 36)
print(lijst)

#8
print(sum(lijst))

#9
lijst.clear()
print(lijst)

#10
lijst.extend([1, 2, 3])
print(lijst)

#11
lijst.extend(range(4,51))
print(lijst)

#12
print(lijst[24])

#13
lijst[0], lijst[-1] = lijst[-1], lijst[0]
print(lijst)

#14
lijst2 = [1, "aap", 2, "apen", 3, "watermeloen", 15, 27, 15, "lekker bezig", "6"]
result = [val for val in lijst2 if isinstance(val, (int))]
print(result)


