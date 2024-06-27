#property in python
class Car:
    def __init__(self,model,price):
        self.__model=None
        self.__price=price
    @model.setter
    def  set_model(self,model):
        self.__model=model
    @property 
    def get_model(self):
        return self.__model
    @price.setter
    def set_price(self,price):
        self.__price=price
    @property
    def get_price(self):
        return self.__price
    def show(self):
        print(self.__model,self.__price)
c=Car()
c.set_model('nexon')
c.set_price(500)
c.model="BMW"
c.price=2000000

print(c.model(),c.price())