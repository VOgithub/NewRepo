print("*** Arvu mängut ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisesta terve arv => "))))
        break
    except ValueError:
         print("See pole terve arv!")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Ära mängu nulliga! ")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Vaatame, kui palju siin paaris ja paaritu arve:")
    print()
    c=b=a                                                         # viga!  vaja =, oli ==
    paaris =0                                                     # viga!  vaja =, oli ==
    paaritu = 0                                                   # viga!  vaja =, oli ==
    while b > 0:                                                  # viga!  vaja : , oli ;
            if b % 2 == 0:                                        # viga!  vaja ==, oli =
                paaris += 1                                #viga! oli =+, vaja +=
            else:
                paaritu += 1                                #viga! oli =+, vaja +=
            b = b // 10
    
    print(" Kui palju paaris arvu:",paaris)                #viga! Pole ","         # skolko Чётных цифр
    print(" Kui palju paaritu arvu :",paaritu)              #viga! Pole ","         # skolko Нечётных цифр
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Vahetatud arvu:")
    print()
    b=0
    while a > 0:                                            # viga!  vaja : 
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Vahetatud arvu", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(("Chekame Siracuse hupotesa: "))
    print()
    if c % 2 == 0:                                          # viga!  vaja ==, oli =
        print("{0} - paaris arvu. Jagame 2...".format(c) )          # vale argumentid in print
    else:
        print("{0} - paaritu arvu. Korrutage 3-ga, lisage 1 ja jagage 2-ga...".format(c))           # vale argumentid in print
    while c != 1:
            if c % 2 == 0:                                  # viga!  vaja ==, oli =
                c = c / 2                                  # viga!  vaja =, oli ==
            else:
                c = ((3*c) + 1) / 2                           # viga!  vaja =, oli ==
            print("{0}. ".format(c))                  # vale argumentid -    print(c, end=")
    print()
    print("Hupotesa on õige!")                                 # viga! vale ´´
