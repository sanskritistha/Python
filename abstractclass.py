#create an abstract class Animal with one abstract method makesound().
#create the derived class Dog,Cat from animal ,instantiate them and call makesound()
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass

class Dog(Animal):
    def makesound(self):
        print('Bark')

class Cat(Animal):
    def makesound(self):
        print('Meow')
d=Dog()
d.makesound()
c=Cat()
c.makesound()
