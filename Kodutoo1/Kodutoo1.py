#Kodutoo 1  TARgv23 Orlov V.
import math 
a = 0
b = 0
# ulesanne 1
# Kirjuta programm, mis sind tervitab.
print (" Ulesanne 1")
print(" Hello, friend from TARgv23!\n")

#Ülesanne 2
#  в выражении сначала нужно выполнить все операции в скобках, затем степени, далее умножение и деление, и, наконец, сложение и вычитание. 
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
print (" Ulesanne 2")
print(" Mis vastus on: 3 + 8 / (4 - 2) * 4  ?")
print( "Esimene samm: (4-2) = 2 ")
a = 4-2
print( "Teine samm: 2 * 4 = 8 ")
a = 2*4
print( "Kolmas samm: 3 + 8 = 11 ")
b = 11
a = b/a
print( "Neljas samm ja vastus on : 11 / 8 = {} \n".format(a))



#Ülesanne 2.1
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala    S = π × r2, , ringi ümbermõõt  l=π*d.
R =C = F =0
print (" Ulesanne 2.1")
R=float(input("Ruudu sees asub ring. Ringi raadius on R. Sisesta R: " ))
print (" Ruudu pindala = {:.2f}. sm".format((2*R)*(2*R)))
print (" Ruudu ümbermõõt = {:.2f}. sm".format(R*8.4))                     #ok
print (" Ringi pindala  = {:.2f}. sm".format(math.pi * (R**2)))
print (" Ringi ümbermõõt = {:.2f}. sm\n".format (math.pi * (R*2)))

# Ülesanne 2.2
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu:
#  kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist,
#   et Maa raadius ekvaatori kohal on 6378 km. 

print (" Ulesanne 2.2")
F = math.pi * (6378 * 2)
print (" Maa ümbermõõt ekvaatori kohal on - {:.3f} km.".format (F,3))
C = 38.83*1000
print (" kui palju 2-euroseid münte tuleb panna üksteise kõrvale in 1 km - {:.1f} tk.".format(C) )
C = C * F
print (" kui palju 2-euroseid münte tuleb panna üksteise kõrvale in Maa ümbermõõt ekvaatori kohal on  - {:.1f} tk\n.".format(C))


#Ülesanne 3
#Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
#kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll
#kill-koll

#Kas kasutasid muutujaid? Millistel juhtudel oleks muutujate kasutamine kindlasti otstarbekas?
a=b=C=F=0
print (" Ulesanne 3")
for a in range (1,10,1):
    if (a==3):
        print(" killadi-koll ")
    elif a==6:
        print(" killadi-koll ")
    else:
        print(" kill-koll ")
print("\n")

#Ülesanne 4
#Koosta programm, mis väljastaks järgmised laulusõnad:

# Не совсем ясно, что хотят получить в задании ???????
print (" Ulesanne 4")
print (" Rong see sõitis tsuhh tsuhh tsuhh,\n piilupart oli rongijuht.\n Rattad tegid rat tat taa, ")
print (" rat tat taa ja tat tat taa.\n Aga seal rongi peal,\n kas sa tead, kes olid seal?\n \n")

print(" Rong see sõitis tuut tuut tuut,\n piilupart oli rongijuht.\n Rattad tegid kill koll koll,\n kill koll koll ja kill koll kill.\n")

# Ülesanne 5
# Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.
print (" Ulesanne 5")
a=b=C=0
print (" On olemas ristkülik, kus on A ja B - katetid...")
a=float(input("Siis sisesta A: " ))
b=float(input("Siis sisesta b: " ))
C=(2*a)+(2*b)
print ("Siis ristküliku perimeter on : {:.2f}".format(C))
F=a*b
print ("Siis ristküliku pindala on : {:.2f}\n".format(F))

# Ülesanne 6
#  Kütusekulu arvutamine

#    Kasutaja sisestab tangitud kütuse liitrid
#    Kasutaja sisestab läbitud kilomeetrid
#    Programm leiab kütusekulu 100km kohta keskmiselt
a=b=C=F=0
fA = 0.0
print (" Ulesanne 6")
print(" Ok, nüüd provime kütusekulud arvutada...")
fA=float(input("Siis sisesta kui palju liitrid : " ))
b=float(input("Siis sisesta kui palju km sõidsid: " ))
C = b / fA    # kui palju km/l
print(" Kulud on km/l ={:.2f}".format(C))
F = 100 / C 
print ("Keskmine kütuse kulud 100 km peale on - {:.2f} l.\n".format (F))

#Ülesanne 7
#Rulluisutajad

#    Rulluisutaja keskmine kiirus on 29,9km/h
#    Kui kaugele jõuab M minutiga

fB =fR= 0.0
print (" \nUlesanne 7")
fB=float(input("Kui palju minutid laheb Rulluisutaja?: " ))
fR = (29.9/60.0)*fB
print (" Rulluisutaja jõuab {:.1f} minutiga {:.3f} kaugele".format (fB,fR))


#Ülesanne 8
#Ajateisendus
#    Kasutaja sisestab aja minutites #    Sinu valem leiab ja väljastab tunnid ja minutid #    Näiteks: sisestus 72, vastus 1:12

print (" \nUlesanne 8")
a=b=C=F=0
a=int(input("Sisesta siis kui palju minutid: "))
b= a//60
C= a% 60
print(" Sa sisestad {0} tunnid ja {1} minutid!\n".format(b,C))






#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

