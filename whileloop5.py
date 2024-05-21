#to input a number and find its reverse
n=int(input('Enter a number'))
sum=0

while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
print("the number is=",sum)


