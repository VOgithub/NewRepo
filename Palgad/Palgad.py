from Funktsioonid import *

palgad=[1200,2500,1300,2500,1200]
inimesed=["A","B","C","D","E"]

for i in range (len(inimesed)):
    print(inimesed[i]," saab katte ", palgad[i])

while True:

    print("\n")
    print("Lisamine-1\nKustuta -2\nSuurimPalk-3\nVahemPalk-4\nSorterimine-5\nKeskminePalk-6\nNimiOtsing-7\n")
    v=int(input("Mis punkt valime?"))
  
    if v==1:
        k=int(input("Mitu inimesed lisame? "))
        inimesed,palgad=Lisamine(inimesed,palgad,k)
        for i in range (len(inimesed)):
            print(inimesed[i]," saab katte ", palgad[i])
    elif v==2:
        inimesed,palgad=Kustuta(inimesed,palgad)
        for i in range (len(inimesed)):
            print(inimesed[i]," saab katte ", palgad[i])

    elif v==3:
        maxpalk,nimi=SuurimPalk(inimesed,palgad)
        print(nimi, " saab katte ", maxpalk, "Euro")
    
    elif v==4:
        minpalk,nimi=VahemPalk(inimesed,palgad)
        print(nimi, " saab katte ", minpalk, "Euro")

    elif v==5:                                     #сортировка
        A=int(input("Kasvab - 0,Kahaneb - 1 ?\n"))
        Sort_nimi,Sort_palk=Sorteerimine(inimesed,palgad,A)
        for i in range (len(inimesed)):
            print(inimesed[i]," saab katte ", palgad[i])
    
    elif v==6:
        keskPalk=keskmine(palgad)                   #средняя зарплата по всему списку!
        print ("Keskmine palk -", round(keskPalk, 2) )

    elif v==7:                                      #поиск по имени
        findPalk,findByName=paring(inimesed,palgad)
        print(findByName," - ", findPalk)
