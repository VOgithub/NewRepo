def Lisamine (i:list,p:list,k:int):
    for x in range (k):
        nimi=input("Mis on inimese nimi?")
        palk=int(input("Kui suur on palk?"))
        i.append(nimi)
        p.append(palk)
    return i,p

def Sorteerimine(inimesed,palgad,A): #A - B>b or b>B
    abi_palk=0
    abi_inimene=" "
    n=len(palgad)
    if A==1:
        for i in range (0,n-1):
            for j in range (i+1,n):
                if palgad[i]<palgad[j]:
                    abi_palk=palgad[i]
                    palgad[i]=palgad[j]
                    palgad[j]=abi_palk
                    abi_inimene=inimesed[i]
                    inimesed[i]=inimesed[j]
                    inimesed[j]=abi_inimene
    else:
        for i in range (0,n-1):
            for j in range (i+1,n):
                if palgad[i]>palgad[j]:
                    abi_palk=palgad[i]
                    palgad[i]=palgad[j]
                    palgad[j]=abi_palk
                    abi_inimene=inimesed[i]
                    inimesed[i]=inimesed[j]
                    inimesed[j]=abi_inimene
    return inimesed,palgad

def Kustuta(i:list,p:list):
    nimi_del=input("Sisesta nimi kustutamiseks: ")
    n=i.count(nimi_del)
    if n>0:
        for x in i:
            if x==nimi_del:
                ind=i.index(x)
                i.remove(x)
                p.pop(ind)
    else:
        print("No this name in list!")
    return i,p

def SuurimPalk(i:list,p:list):
    nimi_list=[]
    max_=max(p)
    a=0
    for palk in p:
        if palk==max_:
            ind=p.index(max_,a)
            nimi=i[ind]
            a+=1
            nimi_list.append(nimi)
    return max_,nimi_list     

def VahemPalk(i:list,p:list):
    nimi_list=[]
    min_=min(p)
    a=0
    for palk in p:
        if palk==min_:
            ind=p.index(min_,a)
            nimi=i[ind]
            a+=1
            nimi_list.append(nimi)
    return min_,nimi_list     