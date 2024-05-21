#wap to input a number and check wheather it is a palindrome or not
n=int(input('Enter a number'))
rev=0
orginal=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==orginal:
    print("plaindrome")
else:
    print('not plaindrome')
