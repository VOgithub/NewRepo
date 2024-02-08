def FileToList (fileX:str, TmpList:list):
    fOpen=open(fileX,'r',encoding = "utf-8")
    for rida in fOpen:
        TmpList.append(rida.strip())
    fOpen.close()
    return TmpList

def ListToFile(fileX:str,TmpList:list):
    #if isfile(fileX):
    #    remove(fileX)
    fOpen=open(fileX,'w',encoding = "utf-8")
    for rida in TmpList:
        fOpen.write(rida +'\n')
    fOpen.close()

def EditWord(ru:list,es:list):
    wFlag=False
    Xword = str(input("Sisesta sona for edit: ").lower())
    for i in range (len(ru)):
        if Xword == ru[i]:
            ru[i]=str(input("Sisesta uus RU variant: ").lower())
            ListToFile("rus.txt",ru)
            wFlag=True
        else:
            for i in range (len(es)):
                if Xword == es[i]:
                    es[i]=str(input("Sisesta uus Est variant: ").lower())
                    ListToFile("est.txt",es)
                    wFlag=True
    if wFlag == True:
        print("Edit done!")
    else:
        print("Nothing to do...")
    return ru,es
    
def Lisamine (ru:list,es:list):

    #k=int(input("Mitu sonad lisame? "))
    #for x in range (k):
        #if (x+1)<=k:
    ruSona=input("Sona on vene keeles:  ")
    estSona=input("Sna on eesti keeles: ")
    ru.append(ruSona)
    es.append(estSona)
    return ru,es

def Translate (ru:list,est:list):
    TmpN=int(input("Vali 1 - RU > EST, 2 - EST > RU  :"))
    if TmpN ==1:
        Xw=str(input("Sisesta sona RU :"))
        Xw=Xw.lower()
        for i in range(len(ru)):
            if Xw == ru[i]:
                print(Xw," : ",est[i])
    elif TmpN ==2:
        Xw=str(input("Sisesta sona EST :"))
        Xw=Xw.lower()
        for i in range(len(est)):
            if Xw == est[i]:
                print(Xw," : ",ru[i])


       
#menu={}                           # не проверено!
#menu['1']= "Paranda sona"
#menu['2']= "Vaata"
