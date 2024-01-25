def Lisamine (ru:list,es:list):
    k=int(input("Mitu sonad lisame? "))
    for x in range (k):
        ruSona=input("Sona on vene keeles:  ")
        estSona=input("Sna on eesti keeles: ")
        ru.append(strip(ruSona))
        es.append(strip(estSona))
    return ru,es
