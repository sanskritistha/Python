class Employee:
    def __init__(self):
        print('Constructor called')
    def __del__(self1):
        print('destructor Called')
e1=Employee()
del e1
    