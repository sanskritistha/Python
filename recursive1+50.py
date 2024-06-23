#to print 1 to 50 using recursive function
'''def numbers(n):
    if n<=50:
        print(n)
        numbers(n+1)
numbers(1)'''
#to print 50 to 1
def numbers(n):
    if n<=50:
      numbers(n+1)
      print(n)
numbers(1)