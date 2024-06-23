#passing lambda to a filter
numbers=[1,3,7,8,10,15]
result=filter(lambda a:a%2!=0,numbers)
print(list(result))