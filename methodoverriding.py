class Animal:
    def makesound(self):
        print('Generic Animal sound')
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