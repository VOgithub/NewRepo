#Kalkulaator
print ("Kalkulaator  TARgv23 Vlad".center(50))
try:
    a=float(input("Esimene arv: "))
    try:
        b=float(input("Teine arv: "))
        t=input("Math operator: ")
        if t in ["+","-","/","*","**","%","//"]:     # '' 
            if t=="+":
                v=a+b 
            elif t=="-":
                v=a-b 
            elif t=="*":
                v=a*b 
            elif t=="**":
                v=a**b 
            elif t=="/":
                if b==0:
                    v="DIV/0"
                else:
                    v=a/b 
            elif t=="%":
                v=a%b
            else:
                v=a//b 
            print("{0} {1} {2} = {3}".format(a,t,b,v).center(50))           
        else:
            print("Tundmatu märk!")
    except :
            print ("Vale B andmetüüp!")
except :
    print ("Vale A andmetüüp!")




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