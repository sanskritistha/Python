a=int( input('enter a marks of 1st subject'))
b=int( input('enter a marks of 2nd subject'))
c=int( input('enter the marks of 3rd subject'))
t=a+b+c
p=t/3
print("total marks=",t)
print("percentage=",round(p,2))
if a>=50 and b>=50 and c>=50:
    print('pass')
    if p>=80:
        print('distinction')
    elif p>=60:
        print('first division')
    else:
        print('second division')
else:
    print('fail')
