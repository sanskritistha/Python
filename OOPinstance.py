#first class and object program
class Student:
    def config(self):   #config()--> instance method or method
        self.name='Ram'
        self.age=20   # name and age--> instance variables or attributes
    def print(self):
        print(self.name,self.age)
s1=Student()
s1.config()
s1.print()