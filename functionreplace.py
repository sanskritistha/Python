#create a function tha ttakes name of someo countries as argumenr and then replace all 'a' with 'p'.
def myfunction(countries):
    for i in range(len(countries)):
        a=countries[i].replace('a','p')
        countries[i]=a
    print(countries)
mylist=['nepal','japan','korea']
myfunction(mylist)