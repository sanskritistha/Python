#Wap to overload <opeartor to check(compose) two person objects which contain the instance varables name and age
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __lt__(self,other):
        return self.age<other.age
p1=Person('ram',20)
p2=Person('hari',21)
if p1<p2:
    print(p1.name,p1.age)
else:
    print(p2.name,p2.age)
    
