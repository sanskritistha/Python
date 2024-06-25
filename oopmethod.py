#method with parameter
class Student:
    def config(self,name,age):  
        self.name=name
        self.age=age  
    def print(self):
        print(self.name,self.age)
s1=Student()
s1.config('coco',4)
s1.print()
s2=Student()
s2.config('sanskriti',20)
s2.print()