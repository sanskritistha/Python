#create a function check() that takes a word as arguement and check palinfroome or not
def pali(n):
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
pali(1001)
