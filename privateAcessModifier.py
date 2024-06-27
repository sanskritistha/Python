class Student:
    def set(self,name,age):
        self.__name=name
        self.__age=age
    def show(self):
        print(self.__name,self.__age)
s=Student()
s.set('ram',20)  #set is public and can be accessed here
s.show() #show is public and can be accessed here
#print(s.__name,s.__age) # name and age are private and cannot be accessef here