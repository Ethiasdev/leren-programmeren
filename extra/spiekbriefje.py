namen = ["anton", "berat", "cors", "dirk", "bardia"]
leeftijden = [16, 17, 18, 16, 17]

for naam,leeftijd in zip(namen, leeftijden): # of enumerate
    print(f"Hallo {naam}, je bent {leeftijd } jaar oud")