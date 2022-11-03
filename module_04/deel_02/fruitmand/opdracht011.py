from fruitmand import fruitmand
rond = 0
nietRond = 0

x = False
while x == False:
    kleur = input("kies een kleur: ")
    for fruit in fruitmand:
        if fruit['color'] == kleur:
            x = True
            
        
            if fruit['round'] == True:
                rond += 1
                        
            else:
                nietRond += 1
              
            if rond > nietRond:
                print(f"Er zijn {rond - nietRond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
                                    
            elif rond < nietRond:
                print(f"Er zijn {nietRond - rond} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
                                    
            elif rond == nietRond:
                print(f"Er zijn {rond} ronde vruchten en {nietRond} niet ronde vruchten in de kleur {kleur}")
            exit() 
                        
                
    else:
        print(f"{kleur} zit er niet in")
             
    
    