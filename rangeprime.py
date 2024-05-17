#4. to input a number and check prime/composite
count=0
for x in range(1,n+1):
    if n%x==0:
        count+=1
if count==2:
    print('prime')
else:
    print('composite')

#5. to print all prime numbers 100 t0 200

for n in range(100,201): 
  count=0
  for x in range(1,n+1):
    if n%x==0:
        count+=1
  if count==2:
    print(n,end=' ')

 