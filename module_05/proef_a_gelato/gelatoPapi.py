print("Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is.")

def stap1():
    aantal = input("Hoeveel bolletjes wilt u? ")
    try:
        aantal = int(aantal)
        if 1 <= aantal <= 3:
            stap2(aantal)
        elif 4 <= aantal <= 8:
            print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes.")
            nogBestellen = input("Wilt u nog iets bestellen? ")
            if nogBestellen.lower() == "ja":
                stap1()
            elif nogBestellen.lower() == "nee":
                print("Bedankt en tot ziens!")
            else:
                print("Sorry, dat snap ik niet...")
                stap1()
        elif aantal > 8:
            print("Sorry, zulke grote bakken hebben we niet.")
            stap1()
        else:
            print("Sorry, dat snap ik niet...")
            stap1()
    except ValueError:
        print("Sorry, dat snap ik niet...")
        stap1()

def stap2(aantal):
    container = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
    if container.lower() in ["hoorntje", "bakje"]:
        stap3(aantal, container)
    else:
        print("Sorry, dat snap ik niet...")
        stap2(aantal)

def stap3(aantal, container):
    print(f"Hier is uw {container} met {aantal} bolletje(s).")
    nogBestellen = input("Wilt u nog meer bestellen? ")
    if nogBestellen.lower() == "ja":
        stap1()
    elif nogBestellen.lower() == "nee":
        print("Bedankt en tot ziens!")
    else:
        print("Sorry, dat snap ik niet...")
        stap3(aantal, container)

stap1()
