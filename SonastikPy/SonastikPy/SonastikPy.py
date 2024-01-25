from SonastikFunctionsPy import *

Rus=["Понедельник","Вторник","Среда"]
Est=["Esmaspäev","Teisipäev","Kolmapäev"]


while True:

    print("\n")
    print("Translate-1\nSonaLisamine -2\nSonaRedigeerimine-3\nVaataSonad-4\n")
    v=int(input("Mis punkt valime?"))
    
    if v==4:
        for i in range (len(Rus)):
            print(Rus[i]," - ", Est[i])

    elif v==2:
        Rus,Est=Lisamine(Rus,Est)
        for i in range (len(Rus)):
            print(Rus[i]," - ", Est[i])


