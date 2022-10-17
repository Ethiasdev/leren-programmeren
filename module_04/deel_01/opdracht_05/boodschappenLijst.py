bag = {}

while True:
    vraag = input("Wil je een product toevoegen?: ").lower()
    if vraag == "nee":
        break

    product = input("Welke product wil je?: ").lower()
    aantal = int(input(f"Hoeveel {product} wil je?: "))

    if product not in bag:
        bag.update({product: aantal})
        
    elif product in bag:
        bag[product] += aantal

print("-[ BOODSCHAPPENLIJST ]-")
for keys, value in bag.items():
    print(f"{value}x {keys}")
print("-----------------------")
   



