#Praktiline iseseisevtöö "Listid"
# TARgv23 

#Sisestage sõna või laise klaviatuurilt ja loendage, mitu vokaali ja mitu konsonanti selles on.
#Kui on sisestatud lause, loendage ka kirjavahemärgid ja tühikud.
import string
print(" Ülesanne 1")

vokaali="aeuoiüöõä"
konson = "ltprwsdfghkxznmbq"
signit=string.punctuation
vok=0
konsonanti=0
sign =0
while True:
    tekst=input("Sisesta sõna või lause: ")
    if tekst.isdigit():
        break
    else:
        tekst_l=list(tekst)
        for e in tekst_l:
            if e.lower() in vokaali:
                vok+=1
            elif e.lower() in konson:
                konsonanti+=1
            else:
               if e.lower() in signit:
                   sign+=1

print("in tekst Vokaali - {0}, konsonanti - {1}, sümvolid - {2} ".format (vok,konsonanti,sign))
            
print(" \nÜlesanne 2")
#Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.
nimed = " "
named5 = list(nimed)
for x in range(0,4,1):
    nimed = str(input ("Sisesta nimi: "))
    named5.append(nimed) 
    print (nimed, x)
for x in named5:
    print(named5, " , \n")



#3
#l=[11,2,3,1,4,5,2,11,1,6,5,6]
#l_set=set(l)
#print(l_set)
#for e in l_set:
#    print(e*"*")

    

#4  Index

indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Jarve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu",
         "Tartumaa,Põlvamaa,Võrumaa, Valgamaa","Viljandimaa,Jarvamaa, Harjumaa, Raplamaa","Pärnumaa","Länemaa, Hiiumaa,Saremaa"]
while True:
    try :
        index=int(input("Sisesta postindex "))
        if len(str(index))==5:
            break
    except :
        print("Viga!")
print ("Indexi analüüs")

index_list=list(str(index))

s1=index_list[0]

if (int(s1))==1:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")
elif int(s1) == 2:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")
elif int(s1) == 3:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")
elif int(s1) == 4:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")
elif int(s1) == 5:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")
elif int(s1) == 6:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")
elif int(s1) == 7:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")
elif int(s1) == 8:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")
elif int(s1) == 9:
    print("Index kulub - " + str(indexid[int(s1)-1])+ "\n")



# print ("index {0} on {1} pirkonnas", format(index,indexid[s1-1]))

#5

from random import *
X_tmp=0
kokku = randint(2,20)
num_list=[]
for i in range(kokku):
    num_list.append(randint(-100,100))
print(num_list)
print()
print("Len of num_list - " + str(len(num_list)))
while True:
    try:
        kogus=int(input("Mitu positsioonid vahetada ?"))
        if kogus<=(len(num_list)/2):
            break
    except :
        print("Proovi uuesti!")

for i in range (0,kogus,1):
    X_tmp = num_list[i]
    print(str(i),"  ", str(num_list[i])," <-->  ",str(num_list[(len(num_list)-i)-1]))
    #print(X_tmp, "\n")

    num_list[i] = num_list[(len(num_list)-i)-1]
    num_list[(len(num_list)-i)-1] = X_tmp
print("\n Result of #5: ", num_list, "\n\n")


#6
print("Ulesanne 6 \n")
X_tmp=0
i_tmp=0
numeric = randint(2,20)
numeric_list=[]
for i in range(numeric):
    numeric_list.append(randint(0,1000))
    # num_list.append(round(random()*1000,2))

print(numeric_list)
print()
print("Len of numeric_list - " + str(len(numeric_list)))
x_tmp=numeric_list[0]
for i in range(0,numeric,1):
    if numeric_list[i] >> x_tmp :
        i_tmp=i 
#  max_=max(num_list)           nahodim max zna4enie v list
   #n=num_list.index(max_)      n=max_
   #num:list.pop(n)             dell max_
   #max_=max_/len(num_list)      divine on len of num_list
   #num_list.insert(n,max_)      insert max_ in position n
   #print(num_list)

#7
print("Ulesanne 7 \n")

numeric = randint(2,20)
numeric_list=[]
for i in range(numeric):
    numeric_list.append(randint(-1000,1000))
print(numeric_list)
print()
print("Len of numeric_list - " + str(len(numeric_list)))
for i in range(0,numeric,1):
    numeric_list[i] = abs(numeric_list[i]) 

numeric_list.sort()
print(numeric_list)
numeric_list.sort(reverse=True)
print(numeric_list)

#8
print("Ulesanne 8 \n")
loomad = ["крот", "белка", "выхухоль","a", "aa", "aaa", "aaaa", "aaaaa","qweasdqweas", "q", "rteww", "ewqqqqq"]
loom_list=list(str(loomad))
print(loom_list, "\n")

