done = 0
indkøbsliste = []

#Kører så længe at done ikke er lig med færdig
while (done != "færdig"):
    #Skriver hvad din indkøbsliste er
    print("Din indkøbsliste er lige nu:")
    print(indkøbsliste)
    #Spørger om man enten vil tilføje, slette eller være færdig med sin indkøbsliste
    done = input("Vil du tilføj/slet/færdig: ")

    #Hvis done er lig med tilføj. Spørger den om hvad man vil tilføje og den tilføjer det herefter til listen
    if (done == "tilføj"):
        tilføj = input("Hvad vil du tilføje? ")
        indkøbsliste.append(tilføj)
        print("")
    
    #Hvis done er lig med slet
    if (done == "slet"):
        #Hvis længden af indkøbslisten/indkøbslisten er tom vil den du skrive at man ikke har noget i indkøbslisten
        if (len(indkøbsliste) == 0):
            print("Du har ikke noget i din indkøbsliste")
            print("")
        #Hvis man har noget i ens indkøbsliste:
        else:
            #Spørger om hvad man vil slette
            slet = input("Hvad vil slette? ")
            #Hvis det man vil slette ikke er i indkøbslisten vil den retunere at tingen du vil slette ikke er i indkøbslisten
            if (slet not in indkøbsliste):
                print("Tingen du vil slette er ikke i indkøbslisten")
                print("")
            #Ellers hvis tingen man vil slette er i indkøbslisten vil tingen blive slettet
            else:
                indkøbsliste.remove(slet)
                print("Fjernede " + slet + " fra din indkøbsliste")
                print("")
    
    #Hvis done er lig med færdig vil den udskrive ens indkøbsliste og afslutte programmet
    if (done == "færdig"):
        print("")
        print("Din indkøbsliste er: ")
        print(indkøbsliste)