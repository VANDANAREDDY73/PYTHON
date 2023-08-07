num = 14
count = 0
for fa in range(1,num+1):
    if (num%fa == 0):
        count +=1
if (count == 2):
    print('prime number')
else:
    print('not prime number')
