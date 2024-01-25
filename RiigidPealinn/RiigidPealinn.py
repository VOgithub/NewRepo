from inspect import _void
from random import *
def failist_to_dict(f:str):   # из файла в словарь
  riik_pealinn={}             # dict {Riik:Pealinn}         
  pealinn_riik = {}           # dict {Pealinn:Riik}
  riigid=[]                # list
  file=open(f,'r',encoding="utf-8-sig")
  for line in file:
      k,v=line.strip().split('-')        #k - võti, v - väärtus
      riik_pealinn[k]=v 
      pealinn_riik[v]=k 
      riigid.append(k)
  file.close()
  return riik_pealinn, pealinn_riik, riigid
#

def riik_2_pealinn(riik_pealinn:dict,pealinn_riik:dict,riigid:list):
    riik=""
    while (riik != " ") or (pealinn != " "):
        riik=input("Riik: ")
        if riik != " ":
            print(riik_pealinn[riik])

        pealinn=input("Pealinn: ")
        if pealinn != " ":
            print(pealinn_riik[pealinn])

def AddDelete(riik_pealinn:dict,pealinn_riik:dict,riigid:list):
    print("\nAdd (1) or Delete(2) keys/value.\n")
    TmpC=int(input("Enter your choice: "))
    if TmpC == 1:
        NewRiik=str(input("Enter new country: "))
        NewPealinn=str(input("Enter new country capital city: "))
        if NewRiik in riik_pealinn:
            print("This country already in!")
        else:
            riik_pealinn[NewRiik]=NewPealinn
            pealinn_riik[NewPealinn]=NewRiik
            riigid.append(NewRiik)
    elif TmpC==2:
        DelRiik=str(input("Enter country for delete: "))
        if DelRiik in riik_pealinn:
            V= riik_pealinn.get(DelRiik)
            riik_pealinn.pop(DelRiik)
            pealinn_riik.pop(V)
            riigid.pop(DelRiik)
        else:
            print("No this country in dictionary!")
    return riik_pealinn, pealinn_riik, riigid













riik_pealinn,pealinn_riik,riigid=failist_to_dict("riigid_pealinnd.txt")
#for Tmp in riigid:                  # WORKED!
#    print("\n *",Tmp)

#for Tmp1 in riik_pealinn:
#    print("\n ** ", Tmp1)
while True:
    print("\n")
    print("VaataDictionary-1\nVaataRiik_Pealinn-2\nAddRiikPealinn-3\n")
    v=int(input("Mis punkt valime?"))

    if v==1:
        print(riigid)

    elif v==2:
        riik_2_pealinn(riik_pealinn,pealinn_riik,riigid)

    elif v==3:









#riigid=list(riik_pealinn.keys())    # WORKED !!
#print(riigid)



for Tmp in pealinn_riik:
    print("\n *** ", Tmp)