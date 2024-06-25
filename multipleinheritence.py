class Father:
    def fun1(self):
        print('inside father class')
class Mother:
    def fun2(self):
        print('inside mother class')
class Son(Father,Mother):
    def fun3(self):
        print('inside son class')
s=Son()
s.fun1()
s.fun2()
s.fun3()