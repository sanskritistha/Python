# wap to handle valueError
try:
  a=int(input('Enter first number'))
  b=int(input('Enter second number'))
  c=a/b
  print("result=",c)
except ValueError as ve:
    print(ve)