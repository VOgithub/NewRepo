#1.a

Nimi=str(input("Mis su nimi on? : ")).lower()
if Nimi=="juku":
    print("Lähme siis kinno, Juku!")

#1.b
    try:
        vanus=int(input("Kui vana sa oled?: "))
        if vanus < 6 :
            print (" Pileti pole vaja, vaba sisenemine!")
        elif 6<= vanus <= 14 :
            print("Osta lastepilet!")
        elif 15 <= vanus <= 65 :
            print("Osta täispilet!")
        elif 100 > vanus > 65:
            print ("Osta sooduspilet!")
        else:
            if (100 < vanus) or (vanus < 0) :
                print ("Vale vanus sisestatud!")
    except:
        print ("Vale andmetüüp!")
else:
    print("Sa pole Juku!")

#2.0
Nimi1=str(input("Mis teie nimi on? : "))
Nimi2=str(input("Aga mis teie nimi on? :"))
print ("{0}, {1}, te olete pinkinaabrit!".format(Nimi1,Nimi2))

#3.0
A1=float(input("Sisesta esimene seina pikkus: "))
B1=float(input("Sisesta teine seina pikkus: "))
if (A1 > 0  and B1 > 0) :
    Ruut1=A1*B1 
    print("Põranda suurus on: {0}".format(Ruut1))
else :
    print("Vale andmet!")

Price1=float(input("Kui te tahate teha remonti - siis sisesta ruutmetri hind: "))
if (Price1 > 0 ) :
    Price1 = Ruut1*Price1
    print("Ruutmetri hind on : {0}".format(Price1,3))
    if (Price1 >= 700) :
        Auhind = ((Price1 / 100 )*70)  #4.0
        print ("Kui täishind {0} - siis koos 30% soodustusega hind tuleb : {1}".format(Price1,Auhind))
else :
    print ("Vale andmed et arvuta!")

#5.0
Temp=float(input("Mis temperatuur praegu on? "))
if (50 > Temp > 18) :
    print("See on rohkem kui 18, tee alla!")

#6.0
Pikkus=float(input("Mis teie pikkus on? :"))
if (50 > Pikkus > 250) :
    print("Vale pikkus!")
elif 160 <= Pikkus <=50 :
    print("Te olete liiga väike!")
elif 249 <= Pikkus <= 181 :
    print("Te olete liiga suur!")
else : 
    print("Tore pikkus, bro!")
#7.0
Piim=float(input("Kui tahad osta piima - siis kui palju? (või sisesta 0 kui ei taha): "))
Leib=float(input("Kui tahad osta leiba - siis kui palju? (või sisesta 0 kui ei taha): "))
Sai=float(input("Kui tahad osta saiad - siis kui palju? (või sisesta 0 kui ei taha): "))
#int Piim1, Leib1, Sai1
#if Piim != 0 :
  #  A1 = Piim * 0,70
#if Leib != 0 :
  #  B1 = Leib * 0,89
#if Sai != 0 :
  #  Price11 = Sai * 0,45

#kokkuHind= A1+B1+Price11
print("Kõik kraam maksab: piim - {0}tk * 0,70c , leib - {1}tk * 0,89, sai - {2}tk *0,45, kokku - {3} ".format(Piim,Leib,Sai,4 ))




















        
       