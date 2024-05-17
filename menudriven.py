print('1.ADD\n 2.SUB\n 3. MUL\n 4.DIV\n')
a=int(input('enter first number'))
b=int(input('enter the second number'))
choice=int(input('enter your choice(1-4)'))
match choice:
   case 1:
     c=a+b
     print('result=',c)
   case 2:
     c=a-b
     print('result=',c)
   case 3:
     c=a*b
     print('result=',c)
   case 4:
     c=a/b
     print('result=',c)
   case other:
      print("invalid choice")