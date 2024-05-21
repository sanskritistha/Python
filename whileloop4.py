#good number if it contains equal no.of digits
n=int(input('enter a number'))
c0=0
c1=0
while n>0:
    r=n%10
    if r==0:
        c0+=1
    elif r==1:
        c1+=1
    n=n//10
if c0==c1:
   print("good number ")
else:
    print("not a good number")

