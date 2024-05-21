n=int(input('Enter a number'))
rev=0
orginal=n
while n>0:
    r=n%10
    rev=rev+r**3
    n=n//10
if rev==orginal:
    print("armstrong")
else:
  print('not armstrong')