class Student:
    def set(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
s=Student()
s.set('ram',20)  #set is public and can be accessed here
s.show() #show is public and can be accessed here
print(s.name,s.age) # name and age are public and can bea accessef here