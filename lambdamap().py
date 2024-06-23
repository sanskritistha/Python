#without using lambda
def func(n):
    return n**2
numbers=[1,2,3,4,5]
result =map(func,numbers)
print(list(result))

#by using lambda function
numbers=[1,2,3,4,5]
result=map(lambda a:a**2,numbers)
print(list(result))