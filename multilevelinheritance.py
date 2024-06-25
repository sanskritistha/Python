class GrandFather:
    def fun1(self):
        print('Inside Grandfather class')
class Father(GrandFather):
    def fun2(self):
        print('INside father class')
class Son(Father):
    def fun3(self):
        print('Inside Son class')
s=Son()
s.fun1()
s.fun2()
s.fun3()