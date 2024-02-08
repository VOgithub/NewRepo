from SonastikFunctionsPy import *
from os import *
Ru=[]
Es=[]
Rus=FileToList("rus.txt",Ru)
Est=FileToList("est.txt",Es)


while True:

    print("\n")
    print("Translate-1\nSonaLisamine -2\nSonaRedigeerimine-3\nVaataSonad-4\nEXIT - 5\n")
    v=int(input("Mis punkt valime?\n"))
    
    if v==4:
        for i in range (len(Rus)):
            print(Rus[i]," - ", Est[i])

    elif v==2:
        Rus,Est=Lisamine(Rus,Est)
        ListToFile("rus.txt",Rus)
        ListToFile("est.txt",Est)
        for i in range (len(Rus)):
            print(Rus[i]," - ", Est[i])

    elif v==1:
        Translate(Rus,Est)
    elif v==3:
        EditWord(Rus,Est)
    elif v==5:
        break

        



