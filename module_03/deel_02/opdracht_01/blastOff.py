from time import sleep


i = 30
delay = 0.5

print("De lancering gaat van start!")
while i > 0:
    print(i)
    i = i - 1
    sleep(delay)
print("De raket is gelanceerd!!")