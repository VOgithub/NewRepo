nimi=0
vastus=2
pikkus=0
mass=0
indeks=0

print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis teie nimi on? ")
print(nimi,", oi kui ilus nimi!" )
vastus=int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
#print(vastus)
if vastus==0:
    print("Kahju! See on väga kasulik info!")
    print()
elif vastus==1:
    pikkus= int(input(nimi + "! Sinu pikkus (cm) : "))
    mass=  float(input("Anna kaal ka (kg) => "))
    mass=int(mass)     #float >> int
    pikkus=int(pikkus)  #int >> int
    print(pikkus, mass)
    indeks = mass/((pikkus/100)**2)
    print(nimi, "! Sinu keha indeks on:", round(indeks, 1))
    indeks=round(indeks, 1) 
    if indeks <16:
        print("Tervisele ohtlik alakaal!")
    elif 16<=indeks<=18.9:
        print("Alakaal!")
    elif 19<=indeks<=25:
        print("Normaalkaal!")
    elif 25.1<=indeks<=30:
        print("Ülekaal!")
    elif 30.1<=indeks<=35:
        print("Rasvumine!")
    elif 35.1<=indeks<=40:
        print("Tugev rasvumine!")
    elif indeks>=40.1:
        print("Tervisele ohtlik rasvumine!")
        
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

