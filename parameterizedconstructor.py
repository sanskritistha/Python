class Student:
 
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
s1=Student('sanskriti',20)
s1.show()
