#remove item from existing tuple
a=('apple','orange','cherry')
b=list(a)
b.remove('apple')
a=tuple(b)
print(a)