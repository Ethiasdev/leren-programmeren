kaas = input("Is de kaas geel?")
if kaas == "ja":
    gaten = input("Zitten er gaten in?")
    if gaten == "ja":
        duur = input("is de kaas belachelijk duur?")
        if duur == "ja":
            print ("Emmenthaler")
        elif duur == "nee":
            print ("Leerdammer")
    elif gaten == "nee":
        hard = input("is de kaas hard als steen?")
        if hard == "ja":
            print ("Parmigiano Reggiano")
        elif hard == "nee":
            print ("Goudse kaas")
elif kaas == "nee":
    schimmel = input("Heeft de kaas blauwe schmimmel?")
    if schimmel == "ja":
        korst = input("Heeft de kaas een korst?")
        if korst == "ja":
            print ("Blue de Rochbaron")
        elif korst == "nee":
            print ("Foume d'Ambert")
    elif schimmel == "nee":
        korst1 = input("Heeft de kaas een korst?")
        if korst1 == "ja":
            print ("Camembert")
        elif korst1 == "nee":
            print ("Mozzarella")
                
    



                                                      

