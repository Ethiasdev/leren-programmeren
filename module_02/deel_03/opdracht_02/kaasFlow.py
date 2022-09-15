kaas = input("Is de kaas geel?")
if kaas.lower() == "ja":
    gaten = input("Zitten er gaten in?")
    if gaten.lower() == "ja":
        duur = input("is de kaas belachelijk duur?")
        if duur.lower() == "ja":
            print ("Emmenthaler")
        elif duur.lower() == "nee":
            print ("Leerdammer")
    elif gaten.lower() == "nee":
        hard = input("is de kaas hard als steen?")
        if hard.lower() == "ja":
            print ("Parmigiano Reggiano")
        elif hard.lower() == "nee":
            print ("Goudse kaas")
elif kaas.lower() == "nee":
    schimmel = input("Heeft de kaas blauwe schmimmel?")
    if schimmel.lower() == "ja":
        korst = input("Heeft de kaas een korst?")
        if korst.lower() == "ja":
            print ("Blue de Rochbaron")
        elif korst.lower() == "nee":
            print ("Foume d'Ambert")
    elif schimmel.lower() == "nee":
        korst1 = input("Heeft de kaas een korst?")
        if korst1.lower() ( "ja"):
            print ("Camembert")
        elif korst1.lower() == "nee":
            print ("Mozzarella")
                        
    



                                                      

