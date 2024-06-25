#create a class stuent with instance variables name,age,faculty.create a parameterized method set()  to set student details 
#and a method show() to print student details create 2 student objects,set the details and print them
class Student:
    def set(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
    def show(self):
        print(self.name,self.age,self.faculty)
s1=Student()
s1.set('sanskriti',20,"BIM")
s1.show()
s2=Student()
s2.set('shrestha',20,'BIM')
s2.show()

        