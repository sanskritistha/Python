#wap to overload + operator to add two point objects that contains the instance variables x and y
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):#self-->p1,other-->p2
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)


p1=Point(5,20)
p2=Point(65,125)
p3=p1+p2#+ call add operator
print(p3.x,p3.y)