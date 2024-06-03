#add item to existing tuple
a=('apple','orannge')
b=list(a)
b.append('mango')
a=tuple(b)
print(a)