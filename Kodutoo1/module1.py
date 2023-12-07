
text=input ("sisesta tekst: ")
text_list = list(text)
if text.isdigit():
    for t in text_list:
        text_list.remove(t)
        t=int(t)
        text_list.append(t)



print (text)

