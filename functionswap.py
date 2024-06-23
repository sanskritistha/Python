#create a function that swaps the two values provided and returns the swaped values
def swap(a,b):
    c=a
    a=b
    b=c
    return a,b
a=5
b=6
print(swap(a,b))
