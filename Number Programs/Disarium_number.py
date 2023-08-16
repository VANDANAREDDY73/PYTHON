num = 135
p=len(str(num))
res=0
copy = num
while(num!=0):
    rem=num%10
    res+=rem**p
    num//=10
    p-=1
if (copy==res):
    print('disarum number')
else:
    print('not disarium number')
