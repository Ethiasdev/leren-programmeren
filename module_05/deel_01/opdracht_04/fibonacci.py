def fibonacci(aantal: int) -> list:
    lijst = [0,1]
    for i in range(aantal):
        lijst.append(lijst[i] + lijst[i + 1])
    snede = lijst[-1] + lijst[-2]
    return snede

print(fibonacci(10))



        
        


    

