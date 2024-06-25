
class Person:
    def setP(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
class Student(Person):
    def setS(self,faculty):
        self.faculty=faculty
    def show(self):
        super().show()# super class is used in derived class only
        print(self.faculty)
s1=Student()
s1.setP('sanskriti',20)
s1.setS('BIM')
s1.show()

