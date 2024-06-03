#unpacking
fruits=('apple','orange','mango')
a,b,c=fruits
print(a)
print(b)
print(c)

#we can also use * symbol with varaible name to get remaning
#data item
fruits=('apple','orange','mango')
a,*b=fruits
print(a)
print(b)