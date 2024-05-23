#wap to input a word and reverse it using string slicing
a=input('enter a word')
b=a[-1::-1]
print(b)

#wap to input a word and check whether it is a palindrome word or not
a=input('enter a word:')
b=a[-1::-1]
if a==b:
    print("plaindrome")
else:
    print("not palindrome")
