num=27
res=0
while (num!=0):
    rem=num%2
    res += rem
    num//=2
if (res%2==0):
    print('Evil no')
else:
    print('odius no')
    
