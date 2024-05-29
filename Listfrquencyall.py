#wap to input a astring and count the frequency of all character
sent=input('enter a string: ')
chars=[]
for ch in sent:
    if ch not in chars:
        chars.append(ch)
for ch in chars:
    print(ch,':',sent.count(ch))