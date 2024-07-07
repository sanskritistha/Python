#wap to overload + and - operators to add and subtract two Distance objects that contain the instance variables km and m
class Distance:
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
d1=Distance(765,4)
d2=Distance(567,3)
d3=d1+d2
d4=d1-d2
print(d3.m,d3.km)
print(d4.m,d4.km)
    
    