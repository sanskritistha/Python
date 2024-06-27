#create a clss Car with th eprivate instance vaariables model and price.create getters and setters.create a 
#car objectset the details and print them
class Car:
    def  set_model(self,model):
        self.__model=model
    def get_model(self):
        return self.__model
    def set_price(self,price):
        self.__price=price
    def get_price(self):
        return self.__price
    def show(self):
        print(self.__model,self.__price)
c=Car()
c.set_model('nexon')
c.set_price(500)
print(c.get_model(),c.get_price())
