#wap to input a word and count the no.of vowels
count=0
a=input('enter a word:')
for x in a:
 if x=='a'or x=='b'or x=='e'or x=='i'or x=='o'or x=='u':
  count+=1
print("no.of vowels=",count)


'''count=0
a=input('enter a word:')
vowels=['a','e','i','o','u']
for x in a:
  if x in vowels:
    count+=1
print("no.of vowels=",count)'''


