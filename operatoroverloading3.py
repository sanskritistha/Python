#Repaat operatoroverloading2, however for km and m, take input for two distance objects and initialize themclass Distance:
class   Distance:
    def __init__(self,km,m):
        self.km=km
        self.m=m
    def __add__(self,other):
        m=self.m+other.m
        km=self.km+other.km+m//1000
     
        m=m%1000
        return Distance(m,km)
    def __sub__(self,other):
        m=self.m-other.m
        km=self.km-other.km+m//1000
        m=m%1000
        return Distance(m,km)
a=int(input("enter km"))
b=int(input("enter meter"))
c=int(input('enter km for 2nd:'))
d=int(input("enter meter for 2nd"))
d1=Distance(a,b)
d2=Distance(c,d)
d3=d1+d2
d4=d1-d2
print(d3.m,d3.km)
print(d4.m,d4.km)