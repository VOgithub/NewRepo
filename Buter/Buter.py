#Buter
Soov=input("Kas tahad süüa? :").lower()
if Soov=="y" or Soov=="да":
    valik =int(input("1- juustuga\n2- vorstiga..?"))
    if valik in [1,2]:
        if valik==1:
            print(" Palun juustuga!")
        else:
            print("Palun vorstiga")
    else:
        print("Vale valik!")
else:
    print("Ei taha, siis ei taha..")
