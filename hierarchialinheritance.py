class Father:
    def fun1(self):
        print('inside father class')
class Son(Father):
    def fun2(self):
        print('inside son class')
class Daughter(Father):
    def fun3(self):
        print('inside daughter class')
s=Son()
s.fun2()
s.fun1()
d=Daughter()
d.fun3()
d.fun1()