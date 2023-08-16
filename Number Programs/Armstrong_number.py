num=153
p=len(str(num))
res=0
copy = num
while (num!=0):
    rem = num%10
    res += rem**p
    num//=10
if (copy==res):
    print('armstrong number')
else:
    print('not armstrong number')
