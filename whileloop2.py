#count no of digits
n=int(input('Enter a number'))
count=0
while n>0:
    count+=1
    n=n//10
print('No of digits=',count)