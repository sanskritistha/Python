count=0
a=input('enter a word:')
vowels=['a','e','i','o','u']
for x in a:
  if x  not in vowels:
    count+=1
print("no.of consonants=",count)