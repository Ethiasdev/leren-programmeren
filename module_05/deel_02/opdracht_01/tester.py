import random
naamlijst = ['kaas', 'vaas', 'laas']
random.shuffle(naamlijst)
naam = []
i = 0
naam.append(naamlijst[-1])
for tees in naamlijst:
    if naamlijst[-1] == naamlijst[i]:
        break
    naam.append(naamlijst[i])
    i += 1

k = 0
for i in naamlijst:
    print(f"{naam[k]} heeft {naamlijst[k]} getrokken")
    k += 1

