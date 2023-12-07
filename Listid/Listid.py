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
l=[11,2,3,1,4,5,2,11,1,6,5,6]
l_set=set(l)
print(l_set)
for e in l_set:
    print(e*"*")

    

    e



