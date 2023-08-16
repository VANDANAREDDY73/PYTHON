num = 145
copy,res = num,0
while (num!=0):
    rem=num%10
    fact = 1
    for x in range(1,rem+1):
        fact *= x
    res += fact
    num//=10
if (copy==res):
    print('strong number')
else:
    print('not strong number')
