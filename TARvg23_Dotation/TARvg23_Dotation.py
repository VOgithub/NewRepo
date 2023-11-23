print ("Dotatsioon  TARgv23 ".center(50))
Grupp = (input("Sisesta teie gruppinimi: "))
if Grupp =="TARgv23":
   Puudumised=int(input("Mitu puudumist sul on? : "))
   if Puudumised < 15:
       hinne=float(input("Mis on sinu keskmine hinne? : "))
       if hinne > 3.8:
           print("Toetus OK!")
       else:
           print("Liiga madal keskmine hind. No toetusi sulle!")
   else:
       print("Toetus ei määratakse")
else:
    print("Teie jaoks pole raha!")

#