import random   # подгружаем
while True:
    user_select = input("Vali oma variant: (kivi, paber, kaarid): ")
    variants = ["kivi", "paber", "kaarid"]
    comp_select = random.choice(variants)
    print(f"\nSa valid - {user_select}, Computer valid - {comp_select}.\n")

    if user_select == comp_select:
        print(f"Molemad valid {user_select}. Mangu loosimine!")
    elif user_select == "kivi":
        if comp_select == "kaarid":
            print("Kivi loo kaarid! Sinu voit!")
        else:
            print("Paber loo kivi! Sa kadunud!")
    elif user_select == "paber":
        if comp_select == "kivi":
            print("Paber loo kivi! Sinu voit!")
        else:
            print("Kaarid loikad paber... Sa kadunud!")
    elif user_select == "kaarid":
        if comp_select == "paber":
            print("Kaarid loikad paber...  Sinu voit!")
        else:
            print("Kivi loo kaarid! Sa kadunud!")

    Mang_again = input("Mangime veel? (y/n): ")        #еще раз?
    if Mang_again.lower() != "y":
        print(f"\nKohtumiseni!\n")
        break