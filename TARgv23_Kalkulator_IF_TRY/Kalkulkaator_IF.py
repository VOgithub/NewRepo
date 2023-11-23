#Kalkulaator
try:
    a=float(input("Esimene arv:"))
except :
    print ("Vale A andmetüüp!")


try:
    t=input("Math operator: ")
    if t in [´+´,´-´,´/´,´*´,´**´,´%´,´//´]:     # '' ili ""
        try:
            b=float(input("Teine arv:"))
        except :
            print ("Vale B andmetüüp!")

    else:
        print("Tundmatu märk!")
















#a=float(input("Alpha:"))
#b=float(input("Beta:"))
#c=float(input("Gamma:"))
#if a>0 and b>0 and c>0:
#    if a+b+c==180:
#        print("Kolmnurk!")
#    else:
#        print("Simple nurgad..")
#else:
#    print("Vale andmed!")