#to find sum of first 50 natural numbers
sum=0
for x in range(1,51):
    sum=sum+x
print('sum= ',sum)
# 2. to find sum of first n natural numbers
n=int(input('enter a number'))
sum=0
for x in range(1,n+1):
    sum=sum+x
print(' the sum= ',sum)

#3. to input a number and finds its factorial
a=int(input('enter a number'))
fact=1
for x in range(1,a+1):
    fact=fact*x
print(' the factorial = ',fact)


   
