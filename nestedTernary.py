a,b,c=input('enter three numbers').split()
x=int(a)
y=int(b)
z=int(c)
msg=x if x<y and x<z else y if y<x and y<z else z
print(msg)
