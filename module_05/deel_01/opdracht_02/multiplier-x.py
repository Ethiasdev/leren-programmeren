def get_multiplication_table(num):
    table = []
    for i in range(1, 11):
        result = num * i
        table.append(f"{num} x {i} = {result}")
    return table

number = int(input("welke tafel wil je getal weten?? "))

for row in get_multiplication_table(number):
    print(row)
