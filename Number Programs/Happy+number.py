num = 25
res = 0
while (num>9):
    while (num!=0):
        rem = num%10
        res += rem **2
        num//=10
    num!=res
if (num==1):
    print('happy number')
else:
    print('not happy number')
    
