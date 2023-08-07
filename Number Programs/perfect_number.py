num = 24
Sum = 0
for fa in range(1,num):
    if (num%fa == 0):
        Sum += fa
if (num == Sum):
    print('Perfect number')
else:
    print('Not Perfect Number')
