k = 50
b = 50
antwoord = 0

while antwoord < 1000:
    b = f"{b} + {k}"
    k = k + 1
    antwoord = antwoord + k
    print(f"{b} {k} = {antwoord}")