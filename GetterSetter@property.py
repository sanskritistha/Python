#property in python
class Car:
    @property 
    def model(self):
        return self.__model
    @model.setter
    def  model(self,model):
        self.__model=model
    @property
    def get_price(self):
        return self.__price
    @price.setter
    def set_price(self,price):
        self.__price=price
c=Car()
c.Model='scoripo'
c.price=150
print(c.Model,c.Price)


print(c.model(),c.price())
