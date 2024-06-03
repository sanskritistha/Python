#wap to input two numbers,pass them to a function and print all values from first to secind number
def values(a,b):
    for x in range(a,b+1):
        print(x)
x=int(input('enter a first number '))
y=int(input('enter a second number '))
values(x,y)