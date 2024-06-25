#create a class stuent with instance variables name,age,faculty.create a parameterized method set()  to set student 
# details and a method show() to print student details.
# create 5 student objects and print only those records who study in'BIM'
class Student:
    def set(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
    def show(self):
        print(self.name,self.age,self.faculty)
s1=Student()
s1.set('sanskriti',20,"BIM")
s2=Student()
s2.set('nisha',20,'BBA')
s3=Student()
s3.set('anisha',20,'BIM')
s4=Student()
s4.set('pranisha',20,'BCA')
s5=Student()
s5.set('rinisha',20,'BSC')
students=[s1,s2,s3,s4,s5]
for student in students:
    if student.faculty=='BIM':
        student.show()



        