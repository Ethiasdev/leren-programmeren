def my_function(getal):
    list = []
    for k in range(getal):
        list.append(f"Hello from function town {k + 1}! ")
    return list

for i in my_function(7):
    print(i)