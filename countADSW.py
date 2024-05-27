#wap to input s sentence and count no.of alphabets,digits,space,words.
sentence=input('enter a sentences')
alpha=0
digit=0
space=0
for ch in sentence:
 if ch.isalpha():
    alpha+=1
 elif ch.isspace():
    space+=1
 elif ch.isdigit():
    digit+=1
print('alphabet:',alpha)
print('digits:',digit)
print('space:',space)
print('word',space+1)
