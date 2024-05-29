#1.
mylist=["a","b","c","d"]
newlist=[x for x in mylist]
print(newlist)
#2.
# to print  without a
fruits=["apple","mango","cherry","litchi"]
'''newlist=[]
for x in fruits:
    if 'a' not in x:
        newlist.append(x)
print(newlist)'''
# using list comprehension
newlist=[x for x in fruits if 'a' not in x]
print(newlist)
