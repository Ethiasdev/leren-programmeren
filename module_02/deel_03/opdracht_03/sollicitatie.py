print ("-----------------------------------------------------------------")
print ("| Solicitatieformulier Circusdirecteur voor Circus HotelDeBotel |")
print ("-----------------------------------------------------------------")
print ("| Er wordt u een aantal relevante vragen gesteld...             |")
print ("| Gelieve die naar eer en geweten in te vullen.                 |")
print ("| Als blijkt dat u aan de criteria voldoet dan komt u in        |")
print ("| aanmerking voor een serieus sollicitatiegesprek!              |")
print ("| Ontspan maar blijf wakker hier komen de vragen.               |")
print ("-----------------------------------------------------------------")

naam = input ("Wat is uw naam?:")
praktijk = int(input("Hoeveel jaar heeft u praktijkervaring met dieren-dressuur?:"))
diploma = input ("Bent u in bezit van een Diploma MBO-4 ondernemen? ja/nee:")
rijbewijs = input ("Bent u in bezit van een geldig Vrachtwagen rijbewijs? ja/nee:")
hoed = input ("Bent u in bezit van een hoge hoed? ja/nee:")
manVrouw = input ("Bent u een vrouw of een man?:")

if manVrouw == "man":
    snor = int(input ("Hoelang is uw snor? (in cm):"))
elif manVrouw == "vrouw":
    krullen = int(input ("Hoelang zijn uw krullen? (in cm):"))

lengte = int(input ("Wat is uw lengte? (in cm):"))
gewicht = int(input ("Wat is uw gewicht? (in kg):"))
certificaat = input ("Heeft u een overleven met een gevaarlijk persoon certificaat? ja/nee:")
veter = input ("Heeft u een Veterstrikdiploma? ja/nee:")
voorhoofd = input ("Heeft u een lange voorhoofd? ja/nee:")
kaas = input ("Heeft u ooit kaas gegeten? ja/nee:")

if praktijk > 4 and diploma == "ja" and rijbewijs == "ja" and hoed == "ja" and snor > 10 or krullen > 20 and lengte > 150 and gewicht > 90 and certificaat == "ja" and veter == "ja" and voorhoofd == "ja" and kaas == "ja":
    print ("Proficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV!")
elif praktijk < 4 or diploma == "nee" or rijbewijs == "nee" or hoed == "nee" or snor < 10 or krullen < 20 or lengte < 150 or gewicht < 90 or certificaat == "nee" or veter == "nee" or voorhoofd == "nee" or kaas == "nee":
    print ("U voldoet niet aan onze strenge eisen voor de functie van Circusdirecteur, het spijt ons!") 