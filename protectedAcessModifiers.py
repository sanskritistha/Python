class Student:
    def set(self,name,age,faculty):
        self.__name=name #name is private
        self._age=age  #age is protected
        self.faculty=faculty #faculty is public
class Parttimestudent(Student):
    def show(self):
        #print(self.__name) -->eRROR
        print(self._age)
        print(self.faculty)
s=Parttimestudent()
s.set('ram',20,'BIM')
s.show()
