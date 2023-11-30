from abc import ABC, ABCMeta
from math import *
import random
#from math import mod, div



#for x in range (10):
#    R = float(input("{0}.R: ".format(x)))
#    if R>0:
#        S=pi*R**2
#    else:
#        S="R peab olla >> 0"
#    print("S={0}".format(S))

x=0
#while x<10:
#    x+=1
#    R=float(input("{0}.R: ".format(x)))
#    if R>0:
#        S=pi*R**2
#    else:
#        S="R peab > 0!"
#    print ("S{0}={1}".format(x,S))


t=0
#for x in range (5):
#    A=float(input("Sisesta A:"))
#    if A.is_integer(): #== true:
#        t+=1
#        print(t)

#3       Вводят 8 чисел. Найти их произведение (только положительных).
#p=1
#lause=""
#for x in range (8):
#    A=float(input("{0}.samm\nSisesta A: ".format(x+1)))
#    if A>0:
#        p*=A 
#        lause=lause+str(A)+"*"
#print (lause[:-1],"=",p,end="")
#print("End.\n")






    # 2.    Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.

B=0
#A=int(input("{0}.Insert A:".format(x) ))
#if A>1:
#    for x in range (A+1):
#        B= B+x
#        print(x, " - B=",B)
#print(" Summ from 0 to {0}: {1}".format(A,B))


    # 3.    Вводят 8 чисел. Найти их произведение (только положительных).

B=1
#for x in range (8):
#    A=int(input("{0}.Insert int:".format(x) ))
#    if A>0:
#        B=B*A 
#        print(x, " - B=",B)
#print(" * of 0 to {0}: {1}".format(7,B))


# 4.    Составьте программу, выводящую на экран квадраты чисел от 10 до 20.

for x in range (10,20+1,1):
    print ("{0}".format(x*x))
print("End.\n")

 #   9.    В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?
#print("Ulesanne 9.")
#A=float(input("{0}.Kui palju euro in pank? ".format(x)))
#B=int(input("{0}.Kui palju aega?".format(x)))
#if A>0:
#    if B>0:
#        for x in range (1,B+1,1):
#            A = A + ((A/100)*3)
#            print ("{0}aasta 3% summ = {1}".format(x,A))
#    else:
#        print("No aasta!")
#else:
#    print("No raha!")
#print("End.\n")

#  15.Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
#0 1 2 3 4 5 6 7 8 9
#0 1 2 3 4 5 6 7 8 9
#...................
#0 1 2 3 4 5 6 7 8 9

y=0
for x in range (0,10,1):
    for y in range(0,10,1):
        print("{0} ".format(y),end="")
    print("\n")
print("End.\n")


#16.Напишите программу, печатающую столбик строк такого вида:
#1 0 0 0 0 0 0 0 0
#0 2 0 0 0 0 0 0 0
#0 0 3 0 0 0 0 0 0
#0 0 0 4 0 0 0 0 0
#0 0 0 0 5 0 0 0 0
#0 0 0 0 0 6 0 0 0
#0 0 0 0 0 0 7 0 0
#0 0 0 0 0 0 0 8 0
#0 0 0 0 0 0 0 0 9

y=0

for x in range (1,10,1):
 #   print("{0} ".format(x),end="")
    for y in range(1,10,1):
        if y==x:
            print("{0} ".format (x), end="")
        else:
            print("0 ",end="")
    #    print("\n")
    print("")
print("\n")
print("End.\n")


#  29.Напишите программу, печатающую столбик строк такого вида:
#x 0 0 0 0 0 0 0 0
#x x 0 0 0 0 0 0 0
#x 0 x 0 0 0 0 0 0
#x 0 0 x 0 0 0 0 0
#x 0 0 0 x 0 0 0 0
#x 0 0 0 0 x 0 0 0
#x 0 0 0 0 0 x 0 0
#x 0 0 0 0 0 0 x 0
#x 0 0 0 0 0 0 0 x

y=0

for x in range (1,10,1):
    print("x ",end="")
    for y in range(1,9,1):
        if y==x-1:
            print("x ", end="")
        else:
            print("0 ",end="")
    print("")
print("\n")
print("End  #29.\n")

# 31.  Губка Боб жарит котлеты. Всего у него К котлет, на одну сковородку помещается М котлет.

###Расчитать сколько сковородок "полных" надо пожарить и сколько котлет останется еще дожарить на последней.
k=0 
m=0

#k=int(input("{0}.Kui palju kotlett on?: ".format(k) ))
#m=int(input("{0}.Kui palju panni peale mahub?: ".format(m) ))
#t=k%m 
#B=k//m
#print(" Kokku vaja {0} täis panni ja veel {1} kotlett eraldi! ".format(B,t))
#print("\n")
#print("End  #31.\n")


# 13.Найти все натуральные числа от 100 до 1000 кратные 7. И посчитать их колличество и сумму.

y=0
k=0
m=0
for x in range (100,1001,1):
    if x%7 == 0:
        k+=1
        m=m+x 
print("\n Chislo {0}, Koli4estvo kratnih 7 = {1}, summa = {2}".format(x,k,m))
print("End  #13.\n")


#  14.Составьте программу, которая вычисляет произведение чисел от 1 до N. Значение N создается случайным образом.
N=0
m=1
N = random.randint(1,20)
print("N = {0}".format(N))
for x in range (1,N+1,1):
    m=m*x
    print("При x = {0} произведение чисел = {1} ".format(x,m))
print()
print("End  #14.\n")

